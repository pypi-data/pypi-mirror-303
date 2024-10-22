import os
from typing import Any, Dict, Optional, Union

import yaml
from lightning.fabric.loggers import Logger
from typing_extensions import override


class LoggerPropertyMixin:
    @property
    @override
    def name(self) -> str:
        """Gets the name of the experiment.

        Returns:
            The name of the experiment.

        """
        return self._name

    @property
    @override
    def version(self) -> Union[int, str]:
        """Gets the version of the experiment.

        Returns:
            The version of the experiment if it is specified, else the next version.

        """
        if self._version is None:
            self._version = 0
        return self._version

    @property
    @override
    def root_dir(self) -> str:
        """Gets the save directory where the versioned CSV experiments are saved."""
        return self._root_dir

    @property
    @override
    def log_dir(self) -> str:
        """The log directory for this run.

        By default, it is named ``'version_${self.version}'`` but it can be overridden by passing a string value for the
        constructor's version parameter instead of ``None`` or an int.

        """
        # create a pseudo standard path
        version = (
            self.version if isinstance(self.version, str) else f'version_{self.version}'
        )
        return os.path.join(self._root_dir, self.name, version)


class YAMLLogger(LoggerPropertyMixin, Logger):
    def __init__(
        self,
        root_dir: str = './',
        name: str = 'lightning_logs',
        version: Optional[Union[int, str]] = None,
        save_every_k: Optional[int] = 100,
    ):
        LoggerPropertyMixin.__init__(self)
        Logger.__init__(self)
        self._root_dir = root_dir
        self._name = name
        self._version = version
        self._log_file = os.path.join(self.log_dir, 'metrics.yaml')
        self._save_every_k = save_every_k
        self._log_buffer = []

        # Create the log directory if it doesn't exist
        os.makedirs(self.log_dir, exist_ok=True)

        self._auto_step = {}

    @override
    def log_hyperparams(self, params: Dict[str, Any]) -> None:
        with open(self._log_file, 'a', encoding='utf-8') as f:
            yaml.dump({'hyperparameters': params}, f)

    @override
    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None) -> None:
        # Implement auto step functionality
        if step is None:
            metric_hash = '&'.join(sorted(metrics.keys()))
            if metric_hash not in self._auto_step:
                self._auto_step[metric_hash] = 0
            step = self._auto_step[metric_hash]
            self._auto_step[metric_hash] += 1

        log_entry = {'step': step, 'metrics': metrics}
        self._log_buffer.append(log_entry)

        if self._save_every_k is not None and len(self._log_buffer) >= self._save_every_k:
            self._write_buffer_to_file()

    def _write_buffer_to_file(self) -> None:
        with open(self._log_file, 'a', encoding='utf-8') as f:
            yaml.dump(self._log_buffer, f)
        self._log_buffer.clear()

    @override
    def save(self) -> None:
        self._write_buffer_to_file()

    @override
    def finalize(self, status: str) -> None:
        self._write_buffer_to_file()
        log_entry = {'status': status}
        with open(self._log_file, 'a', encoding='utf-8') as f:
            yaml.dump([log_entry], f)
