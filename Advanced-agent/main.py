from dotenv import load_dotenv
from src.workflow import Workflow


load_dotenv()


def main():
    Workflow = Workflow()
    print("Developer Tools Research Agent")


    while True:
        query = input("\n🔍 Developer Tools Query: ").strip()
        if query.lower() in {"quit", "exit"}:
            