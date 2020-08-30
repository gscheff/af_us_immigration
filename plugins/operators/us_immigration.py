from airflow.operators.bash_operator import BashOperator
from airflow.utils.decorators import apply_defaults


class UpsertOperator(BashOperator):

    _templated_command = (
        "cd {{ var.value.project_dir }}/udacity/us_immigration && "
        "pipenv run python -m us_immigration.cli "
        "upsert {{ prev_ds }}"
    )

    @apply_defaults
    def __init__(
            self,
            *args, **kwargs) -> None:
        super().__init__(
            *args,
            bash_command=self._templated_command,
            **kwargs)
