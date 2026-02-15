from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from enum import Enum as PyEnum 
import re
from enum import StrEnum


class Roles(StrEnum):
    HEADMASTER = "HEADMASTER"
    HR = "HR"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"

class Departments(StrEnum):
    SCIENCES = "SCIENCES"
    HUMANITIES = "HUMANITIES"
    LANGUAGES = "LANGUAGES"

class ClassLevel(int, PyEnum):
    form_1 = 1
    form_2 = 2
    form_3 = 3
    form_4 = 4


class Subjects(StrEnum):
    English = "English"
    Mathematics = "Mathematics"
    Physics = "Physics"
    Chemistry = "Chemistry"
    Computer = "Computer"
    Bible_Knowledge = "Bible Knowledge"


class Gender(StrEnum):
    male = "MALE"
    female = "FEMALE"
    other = "OTHER"


class Base(BaseModel):
    username: str
    email: EmailStr
    fullname: str | None = None
    gender: Gender 
    role: Optional[Roles] = None
    department: Optional[Departments] = None

    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",           # prevent extra fields
    )


    @field_validator('username')
    def validate_username(cls, value: str) -> str:
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", value):
            raise ValueError("Username must be 3-20 characters long and contain only letters, numbers, or underscores")
        return value
    
    @field_validator('email')
    def validate_email(cls, value: EmailStr) -> str:
        return value.lower()

    


class CreateUser(Base):
    password: str


class UserResponse(Base):
    id: int


    class Config:
        from_attributes = True




class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    username: str | None = None



class SubjectBase(BaseModel):
    subjectName: str
    enrollment: int

class SubjectResponce(BaseModel):
    id: int
    name: str
    enrollment: int


class DepartmentInfo(BaseModel):
    deptName: Departments
    hod: Optional[str]
    hod_id: Optional[int]
    teacher_count: int = 0
    students_count: int = 0

    model_config = ConfigDict(from_attributes=True)