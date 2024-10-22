from typing import Iterable

from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn
from tqdm import tqdm


def tqdm_progress(iterable: Iterable, description: str):
    return tqdm(iterable, desc=description)


def rich_progress(iterable: Iterable, description: str, color: str = 'green'):
    total = len(iterable)
    with Progress(
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        TaskProgressColumn(),
        TextColumn('{task.completed}/{task.total}'),
    ) as progress:
        task = progress.add_task(f'[{color}]{description}', total=total)
        for i, item in enumerate(iterable, 1):
            yield item
            progress.update(task, advance=1, description=f'[{color}]{description} ({i}/{total})')
