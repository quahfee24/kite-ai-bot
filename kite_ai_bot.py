from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

# Open Kite AI testnet quests
driver.get("https://testnet.gokite.ai/quests")
time.sleep(5)  # Wait for page to load

# Function to interact with an agent
def interact_with_agent(agent_name):
    try:
        button = driver.find_element(By.XPATH, f"//button[contains(text(), '{agent_name}')]")
        button.click()
        print(f"Interacted with {agent_name}")
        time.sleep(10)  # Adjust delay as needed
    except Exception as e:
        print(f"Error interacting with {agent_name}: {e}")

# Interact with all agents
agents = ["Professor", "Sherlock", "Crypto Buddy"]
for agent in agents:
    interact_with_agent(agent)

driver.quit()
print("Bot completed interactions!")
