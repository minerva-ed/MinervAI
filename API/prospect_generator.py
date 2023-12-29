from agents.GeneralAgent import GeneralAgent  # Import GeneralAgent from agents/GeneralAgent.py
import json
import utilities as util

general_agent = GeneralAgent()  # Instantiate a GeneralAgent
async def generate_prospects(product_description: str, sales_profile: str):
    res = await general_agent.get_prospects(product_description, sales_profile)
    print(res.result[7:-3])
    prospects = json.loads(res.result[7:-3])
    return prospects

if __name__ == "__main__":
    import asyncio  # Import asyncio for asynchronous execution
    asyncio.run(generate_prospects(util.load("samples/sales/sample.txt"), "Current customers include MSFT Sales, Rimowa, and Walmart. Generally looking at new b2b saas customers"))  # Run the simulate_classroom coroutine