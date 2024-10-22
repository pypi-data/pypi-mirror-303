from datetime import datetime, timedelta
from typing import List, Optional, Set, TypedDict, Union
from xml.etree import ElementTree as ET

from zyplib.annotation.event import Event


def write_annotationlist_xml(events: List[Event], start_time: datetime, xml_fpath: str):
    """导出 EDFBrowser 的 xml 格式标注文件

    Parameters
    ----------
        - `events` : List[Event]
            - 事件列表, Evnet 为 zyplib.annotation.type.Event 类型; 单位为秒
        - `start_time` : datetime
            - 时间开始时间
        - `xml_fpath` : str
            - 导出的 xml 文件路径
    """
    annotationlist = ET.Element('annotationlist')
    for event in events:
        annotation = ET.SubElement(annotationlist, 'annotation')
        onset = event.onset
        duration = event.duration
        description = event.name
        onset_time = start_time + timedelta(seconds=onset)
        onset_time_str = onset_time.strftime('%Y-%m-%dT%H:%M:%S.%f')
        ET.SubElement(annotation, 'onset').text = onset_time_str
        ET.SubElement(annotation, 'duration').text = str(duration)
        ET.SubElement(annotation, 'description').text = description
    xml_bytes = ET.tostring(
        annotationlist, encoding='UTF-8', xml_declaration=True
    ).replace(b"'", b'"')
    with open(xml_fpath, 'wb') as f:
        f.write(xml_bytes)
