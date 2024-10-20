from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Set, TypedDict, Union
from xml.etree import ElementTree as ET

from zyplib.annotation.event import Event


@dataclass
class ScoredEventType:
    type: int
    name: str

    def __hash__(self) -> int:
        return self.type

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ScoredEventType):
            return self.type == __value.type
        elif isinstance(__value, int):
            return self.type == __value
        elif isinstance(__value, str):
            return self.name == __value
        else:
            return False


@dataclass
class ScoredEvent(ScoredEventType):
    type: int
    name: str
    time: float
    duration: float
    manully_scored: int
    param1: Optional[int] = None
    param2: Optional[int] = None
    param3: Optional[int] = None

    def same_type(self, __value: Union[int, str, ScoredEventType]) -> bool:
        return super().__eq__(__value)

    def to_event(self) -> Event:
        return Event(name=self.name, onset=self.time, duration=self.duration)


class PSGScoredEvents:
    """CMPPSGSCOREDATA XML 文件的读取"""

    def __init__(self) -> None:
        self.base_name: str = None  # 如 'cyq202107220206' 包含了姓名和基本信息
        self.created_on: datetime = None
        self.scored_events: List[ScoredEvent] = []
        self.sleep_stages: List[int] = []

    def push_event_(self, onset, duration, name, type=-1, manually_scored=-1):
        """添加事件"""
        scored_event = ScoredEvent(
            type=type,
            name=name,
            time=onset,
            duration=duration,
            manully_scored=manually_scored,
        )
        self.scored_events.append(scored_event)

    @property
    def unique_events(self) -> Set[ScoredEventType]:
        """获取所有的唯一的事件"""
        return set(
            [
                ScoredEventType(type=score_event.type, name=score_event.name)
                for score_event in self.scored_events
            ]
        )

    def filter(self, *event_types: Union[int, str, ScoredEventType]) -> 'PSGScoredEvents':
        """根据事件类型过滤 scored_events, 并创建一个新的 PSGScoredData

        根据输入的 event_type 来过滤 scored_events, 并创建一个新的 PSGScoredData

        Parameters
        ----------
            - `event_types`: 事件类型, 可以是 int, str, ScoredEventType

        Returns
        ---------
            - `PSGScoredData`: 过滤后的 PSGScoredData
        """
        event_types = set(event_types)
        new_scored_events = []
        for score_event in self.scored_events:
            for event_type in event_types:
                if score_event.same_type(event_type):
                    # print('Same type', score_event)
                    new_scored_events.append(score_event)
        psg_scored_data = PSGScoredEvents()
        psg_scored_data.created_on = self.created_on
        psg_scored_data.scored_events = new_scored_events
        psg_scored_data.sleep_stages = self.sleep_stages
        return psg_scored_data

    def filter_(self, *event_types: Union[int, str, ScoredEventType]):
        """据事件类型过滤 scored_events, 同 `filter`, 但是直接更改 self"""
        psg_scored_data = self.filter(*event_types)
        self.created_on = psg_scored_data.created_on
        self.scored_events = psg_scored_data.scored_events
        self.sleep_stages = psg_scored_data.sleep_stages

    @staticmethod
    def from_xml_file(xml_fpath: str):
        fname = Path(xml_fpath).name
        base_name = fname.split('.')[0]

        # 1. 读取 xml 文件
        tree = ET.parse(xml_fpath)
        # 2. 读取 /SCOREDEVENTS/SCOREDEVENT
        root = tree.getroot()

        score_events = []
        SCOREDEVENTS = root.find('SCOREDEVENTS')
        for scoredevent in SCOREDEVENTS.iter('SCOREDEVENT'):
            score_event = ScoredEvent(
                type=int(scoredevent.find('TYPE').text),
                name=scoredevent.find('NAME').text,
                time=float(scoredevent.find('TIME').text),
                duration=float(scoredevent.find('DURATION').text),
                manully_scored=int(scoredevent.find('MANUALLYSCORED').text),
                param1=int(scoredevent.find('PARAM1').text),
                param2=int(scoredevent.find('PARAM2').text),
                param3=int(scoredevent.find('PARAM3').text),
            )
            score_events.append(score_event)
        # 3. 读取 /SLEEPSTAGES/SLEEPSTAGE
        sleep_stages = []
        for sleepstage in root.findall('SLEEPSTAGES/SLEEPSTAGE'):
            sleep_stages.append(int(sleepstage.text))
        # 4. 返回
        psg_scored_data = PSGScoredEvents()
        created_on_str = root.find('CREATEDON')  # 例如: 2021/7/22 19:47:00
        created_on: datetime = datetime.strptime(created_on_str.text, '%Y/%m/%d %H:%M:%S')
        psg_scored_data.created_on = created_on
        psg_scored_data.scored_events = score_events
        psg_scored_data.sleep_stages = sleep_stages
        psg_scored_data.base_name = base_name
        return psg_scored_data


def read_scoreddata_xml(xml_fpath: str) -> List[Event]:
    psg_events = PSGScoredEvents.from_xml_file(xml_fpath)
    return [event.to_event() for event in psg_events.scored_events]
