from dotenv import load_dotenv
from src.workflow import Workflow


load_dotenv()


def main():
    Workflow = Workflow()
    print("Developer Tools Research Agent")


    while True:
        query = input("\n🔍 Developer Tools Query: ").strip()
        if query.lower() in {"quit", "exit"}:
            break

        
        if query:
            result = Workflow.run(query)
            print(f"\n📊 Results for: {query}")
            print("=" * 60)


            for i, company in enumerate(result.companies, 1):
                print(f"\n{i}. 📅 {company.name}")
                