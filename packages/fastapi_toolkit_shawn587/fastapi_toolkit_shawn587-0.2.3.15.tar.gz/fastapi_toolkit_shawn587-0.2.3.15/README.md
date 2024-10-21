# fastapi_toolkit

## 定义基础模型

### metadata

```python
class Item(Schema):
    field_int: int
    field_float: float
    field_string: str
    field_date: datetime.date
    field_datetime: datetime.datetime
```

### 生成代码

#### schema

```python
class SchemaBaseItem(Schema):
    """pk"""
    id: int = Field(default=None)

    deleted_at: Optional[datetime.datetime] = Field(default=None, exclude=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    """fields"""
    field_int: int = Field()

    field_float: float = Field()

    field_string: str = Field()

    field_date: datetime.date = Field()

    field_datetime: datetime.datetime = Field()


class SchemaItem(SchemaBaseItem):
    """relationships"""
```

#### model

```python
class DBItem(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    field_int: Mapped[int] = mapped_column(sqltypes.Integer, nullable=False)

    field_float: Mapped[float] = mapped_column(sqltypes.Float, nullable=False)

    field_string: Mapped[str] = mapped_column(sqltypes.Text, nullable=False)

    field_date: Mapped[datetime.date] = mapped_column(sqltypes.Date, nullable=False)

    field_datetime: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime, nullable=False)
```

## 定义关联模型
### 一对一 
```python
class Student(Schema):
    name: str
    pass_card: 'PassCard'


class PassCard(Schema):
    account: int
    student: 'Student'
```
Got
```python
class DBStudent(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    name: Mapped[str] = mapped_column(sqltypes.Text, nullable=False)

    _fk_pass_card_pass_card_id: Mapped[int] = mapped_column(ForeignKey("pass_card.id"), nullable=True)

    pass_card: Mapped[Optional["DBPassCard"]] = relationship(
        back_populates="student",
    )


class DBPassCard(Base):
    __tablename__ = "pass_card"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    account: Mapped[int] = mapped_column(sqltypes.Integer, nullable=False)

    student: Mapped[Optional["DBStudent"]] = relationship(
        back_populates="pass_card",
    )
```
### 一对一 多重关联
```python
class Student(Schema):
    name: str
    mentor_teacher: 'Teacher'
    tutor_teacher: 'Teacher'


class Teacher(Schema):
    name: str
    mentor_student: 'Student'
    tutor_student: 'Student'
```
Got
```python
class DBStudent(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    name: Mapped[str] = mapped_column(sqltypes.Text, nullable=False)

    _fk_mentor_teacher_teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"), nullable=True)

    mentor_teacher: Mapped[Optional["DBTeacher"]] = relationship(
        back_populates="mentor_student",
    )

    _fk_tutor_teacher_teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"), nullable=True)

    tutor_teacher: Mapped[Optional["DBTeacher"]] = relationship(
        back_populates="tutor_student",
    )


class DBTeacher(Base):
    __tablename__ = "teacher"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    name: Mapped[str] = mapped_column(sqltypes.Text, nullable=False)

    mentor_student: Mapped[Optional["DBStudent"]] = relationship(
        back_populates="mentor_teacher",
    )

    tutor_student: Mapped[Optional["DBStudent"]] = relationship(
        back_populates="tutor_teacher",
    )
```
> PS: 为了绑定双向关联，关联必须拥有相同的前缀，同时以关联对象的名称(复数)结尾
> 
> mentor_teacher < --- > mentor_student
> 
> mentor_teacher < --- > mentor_students // 当一个老师领导多个学生
> 
> mentor_students显然意义不明，所以可以使用alias特性得到更可读的代码

### 使用alias
```python
class Student(Schema):
    name: str
    mentor: 'Teacher' = Field(alias='mentor_teacher')
    tutor: 'Teacher' = Field(alias='tutor_teacher')


class Teacher(Schema):
    name: str
    mentee: 'Student' = Field(alias='mentor_student')
    trainee: 'Student' = Field(alias='tutor_student')
```
Got

成功绑定关联的同时，获得了更可读的字段名，也不需要遵守必须以目标对象名字结尾的要求

但是alias要遵守规则，同时alias仅用于绑定关联
```python
class DBStudent(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    name: Mapped[str] = mapped_column(sqltypes.Text, nullable=False)

    _fk_mentor_teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"), nullable=True)

    mentor: Mapped[Optional["DBTeacher"]] = relationship(
        back_populates="mentee",
    )

    _fk_tutor_teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"), nullable=True)

    tutor: Mapped[Optional["DBTeacher"]] = relationship(
        back_populates="trainee",
    )


class DBTeacher(Base):
    __tablename__ = "teacher"

    id: Mapped[int] = mapped_column(sqltypes.Integer, primary_key=True, autoincrement=True)
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(sqltypes.DateTime, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)
    updated_at: Mapped[datetime.datetime] = mapped_column(sqltypes.DateTime)

    name: Mapped[str] = mapped_column(sqltypes.Text, nullable=False)

    mentee: Mapped[Optional["DBStudent"]] = relationship(
        back_populates="mentor",
    )

    trainee: Mapped[Optional["DBStudent"]] = relationship(
        back_populates="tutor",
    )
```