from pydantic import BaseModel
from typing import List, Optional, Union, Dict, Set


class GroupModel(BaseModel):
    """группа"""
    group: int = 0
    specialization: str = 'undefined'

    def __hash__(self):
        return hash(self.group)


class PairModel(BaseModel):
    """сущность пары """
    classroom: str = 'undefined'
    subject: str = 'undefined'
    teacher: str = 'undefined'

    def __str__(self):
        return f"{self.classroom} - {self.subject} - {self.teacher}"

    def __hash__(self):
        return hash(self.classroom + self.subject + self.teacher)


# выше две базовые сущности

class AlternatingPairModel(BaseModel):
    """пара мигалка, которая состоит из двух пар"""
    odd_week: Optional[PairModel]  # нечётная неделя
    even_week: Optional[PairModel]  # чётная неделя


class SchedulePairModel(BaseModel):
    """определённая пара в расписании"""
    pair_number: int
    pair: Optional[Union[AlternatingPairModel, PairModel]]


class GroupPairsScheduleModel(BaseModel):
    """расписание группы для определённой группы на неделю"""
    group: GroupModel
    schedule_pairs: Dict[str, List[SchedulePairModel]]


class ScheduleModel(BaseModel):
    specializations_with_groups: Dict[str, List[GroupModel]]
    specializations: Set[str]
    groups: Set[GroupModel]
    classrooms: Set[str]
    teachers: Set[str]
    subjects: Set[str]
    schedule_pairs: List[GroupPairsScheduleModel]
