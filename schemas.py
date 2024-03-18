from sqlmodel import SQLModel, Field


class Todo(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str = Field(max_length=200)
    description: str
    completed: bool = Field(default=False)
