import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://fuksangwong_sit722_part1_user:rvW45XnNP5z1h5G7wmzjcuxbRBDB6Wa8@dpg-cqs3j1ggph6c73a6uaqg-a.oregon-postgres.render.com/fuksangwong_sit722_part1")

settings = Settings()
