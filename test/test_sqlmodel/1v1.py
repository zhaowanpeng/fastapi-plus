# -*- coding: utf-8 -*-
"""
@Time    :  2024/1/2 17:24
@Author  :  Zhao Wanpeng
@Desc    :  None
"""
from typing import List, Optional

from sqlmodel import SQLModel, Field, create_engine, Session, Relationship, select


class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    hero_id: Optional[int] = Field(
        default=None, foreign_key="hero.id", primary_key=True
    )

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


# Code above omitted 👆

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    teams: List[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)



# Code below omitted 👇

# Code below omitted 👇
# Code above omitted 👆

# sqlite_file_name = "database.db"
sqlite_url = "mysql+pymysql://root:1230@localhost/database1"

engine = create_engine(sqlite_url, echo=False)
# SQLModel.metadata.create_all(engine)

def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()
        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    print(1)
    #create_db_and_tables()
    # create_heroes()

    # with Session(engine) as session:
    #     statement = select(Hero).where(Hero.name <= "Tommy Sharp")
    #     results = session.exec(statement)
    #     hero = results.first()
    #     print(hero.team)
    #     print(hero.team_id)
    #     print(hero.team.name)