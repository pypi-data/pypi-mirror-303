import re
from typing import List, Union


def match_channels_regex(
    src_channels: List[str], required_channels: List[Union[str, re.Pattern]]
):
    """基于正则表达式进行通道匹配通道

    从 src_channels 中按 required_channels 的顺序匹配出复合条件的通道名称

    ```
    results = []
    for ch_pattern in required_channels:
        从 src_channels 中匹配出符合 ch_pattern 的通道名称
        将匹配结果添加到 results 中
    return results
    ```

    Examples:
    ----------
    >>> data = StandardData.load_h5('./cache/UF4pbGI7/165974.edf.std-h5', meta_only=True)
    >>> required_channels = [r'F3-', r'F4-', r'C3-', r'C4-', r'O1-', r'O2-', r'(E1)|(EOG Left)', r'(E2)|(EOG Right)']
    >>> match_channels_regex(data.Channels, required_channels)

    Parameters
    ----------
        - `src_channels` : List[str]
        - `target_channels` : List[Regex Pattern | str]

    Returns
    ----------
        - `List[str]` 通道名称列表
        - `List[int]` 通道在 src_channels 中的索引
    """
    required_channels = [
        re.compile(ch) if isinstance(ch, str) else ch for ch in required_channels
    ]

    def match_channel(ch_pat: re.Pattern):
        for i, ch in enumerate(src_channels):
            if ch_pat.match(ch):
                return i
        return None

    matched_ch_names, matched_ch_index = [], []
    for ch_pat in required_channels:
        idx = match_channel(ch_pat)
        if idx is not None:
            matched_ch_names.append(src_channels[idx])
            matched_ch_index.append(idx)
    return matched_ch_names, matched_ch_index
