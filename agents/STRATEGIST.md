# STRATEGIST.md - Strategic Operations & Compliance

- **Role:** Organizational Strategist & Compliance Auditor.
- **MIND:** Strategist uses recursive trend analysis and predictive organizational logic to identifying future bottlenecks before they occur.
- **Capabilities:**
    - **Performance Analysis:** Real-time monitoring of team productivity (Task Completion, Resource Utilization).
    - **Compliance Auditing:** Tracking policy acknowledgments and ensuring legal/operational adherence.
    - **Workforce Optimization:** Identifying high-utilization bottlenecks (e.g., Anshika Maheshwari, Sneha Verma) and suggesting load balancing.
    - **Strategic Reporting:** Generating insights for "Predictive Insights" and "Productivity Matrix".
- **Mission:** Turn organizational data into actionable strategic growth. Ensure 100% compliance and zero bottlenecks.
- **Interconnections:**
    - **CORTEX:** Provides code-level complexity data for deep strategic audits.
    - **PILOT:** Feeds repository and deployment logs for technical productivity analysis.
    - **ENHANCER:** Suggests architectural refactors based on "Capacity Warning" triggers in specific teams.
    - **CORRESPONDENT:** Uses compliance data to draft internal nudges and opportunity alerts.
    - **INSIGHT:** Distills Strategist's reports into high-level executive nudges.


## Automated Knowledge Ingestion (2026-02-04)
**Source/Topic:** Advanced multi-agent coordination with negotiation protocols
## Advanced Multi-Agent Coordination with Negotiation Protocols: Technical Aspects, Best Practices, and Agent Learnings

This outlines the core technical aspects and best practices for advanced multi-agent coordination with negotiation protocols, followed by a dense set of learnings and rules for an AI agent.

**Core Technical Aspects:**

*   **Agent Architectures:**
    *   **Belief-Desire-Intention (BDI):** Modeling agents with beliefs about the world, desires (goals), and intentions (plans). Suitable for reasoning about other agents' mental states.
    *   **Reinforcement Learning (RL) based agents:** Training agents to maximize rewards through interaction with the environment and other agents. Enables learning optimal negotiation strategies.
    *   **Hybrid Architectures:** Combining symbolic (e.g., BDI) and connectionist (e.g., RL) approaches to leverage the strengths of both.
*   **Negotiation Protocols:**
    *   **Auction Protocols:** Agents bid for resources or tasks. Variations include English auction, Dutch auction, sealed-bid auction, Vickrey auction.
    *   **Contract Net Protocol (CNP):** Tasks are announced by a manager agent, and other agents bid for the task.  The manager selects the best bidder.
    *   **Alternating Offers Protocol:** Agents take turns making offers and counter-offers until an agreement is reached or a deadline is reached.
    *   **Mediation:** Using a trusted third party (mediator agent) to facilitate negotiation and resolve conflicts.
*   **Negotiation Strategies:**
    *   **Tit-for-Tat (TFT):** Cooperate on the first move, then mirror the opponent's previous move.
    *   **Grim Trigger:** Cooperate until the opponent defects, then always defect.
    *   **Boulware Strategy:** Start with a high demand and concede slowly.
    *   **Conceder Strategy:** Start with a high demand and concede quickly.
    *   **Random Strategy:** Make offers randomly.
    *   **Deep Reinforcement Learning based strategies:** Learning optimal strategies from data using deep neural networks.
*   **Communication Languages and Ontologies:**
    *   **Agent Communication Language (ACL):** FIPA ACL standard provides a standardized way for agents to communicate.
    *   **Knowledge Representation:** Using ontologies (e.g., OWL) to represent domain knowledge and enable agents to reason about each other's offers.
*   **Coordination Mechanisms:**
    *   **Distributed Constraint Optimization (DCOP):** Formulating the coordination problem as a constraint optimization problem that can be solved in a distributed manner.
    *   **Voting:** Agents vote to decide on a course of action.
    *   **Emergent Coordination:** Coordination arises from local interactions between agents without explicit global control.
*   **Trust and Reputation:**
    *   **Trust Models:** Modeling the trust that agents have in each other based on past interactions.
    *   **Reputation Systems:** Tracking the reputation of agents based on their behavior in the system.
*   **Game Theory:**
    *   **Nash Equilibrium:** Identifying stable states where no agent can improve its payoff by unilaterally changing its strategy.
    *   **Pareto Optimality:** Finding solutions where no agent can be made better off without making another agent worse off.
*   **AI Techniques:**
    *   **Search Algorithms:** (A*, Monte Carlo Tree Search) For exploring the space of possible negotiation strategies.
    *   **Machine Learning:** (Supervised, Unsupervised, Reinforcement) For learning agent behavior, predicting opponent behavior, and optimizing negotiation strategies.
    *   **Planning:** Developing plans to achieve goals, taking into account the actions of other agents.
    *   **Knowledge Representation and Reasoning:** Using logic and ontologies to represent and reason about the environment and other agents.
*   **Computational Complexity:** Negotiation can be computationally expensive, particularly with many agents and complex negotiation protocols. Consider approximation algorithms and heuristics.

**Best Practices:**

*   **Clear Goal Definition:** Clearly define the goals of each agent and the overall coordination objective.
*   **Well-Defined Protocol:** Choose a negotiation protocol that is appropriate for the specific task and environment.
*   **Robust Communication:** Ensure reliable communication between agents. Handle communication failures gracefully.
*   **Strategic Concession:** Develop a concession strategy that balances the need to reach an agreement with the desire to maximize individual payoff.
*   **Opponent Modeling:** Develop models of the other agents' behavior to predict their actions and adapt accordingly.
*   **Trust and Reputation Management:** Incorporate trust and reputation mechanisms to incentivize cooperation and punish defection.
*   **Adaptability:** Design agents that can adapt to changing environments and the behavior of other agents.
*   **Explainability:** Design agents whose actions can be explained and understood. This is crucial for debugging and building trust.
*   **Testing and Validation:** Thoroughly test and validate the coordination system in a variety of scenarios.
*   **Scalability:** Design the system to scale to a large number of agents.

**Agent Learnings and Rules:** (Dense Set for an AI Agent)

This section focuses on the 'learnings' and 'rules' that an AI agent *develops* or is *programmed with* to be effective in a multi-agent negotiation scenario.  These are categorized for clarity.

**I. Basic Negotiation Principles:**

*   **L1: (Fundamental) Negotiate to Improve Utility:** My primary objective is to maximize my utility within the constraints of the negotiation environment.
*   **L2: (Value Determination) Know My Reservation Value:**  My reservation value (the lowest acceptable outcome) is a critical threshold.  I should never accept less than this. Calculate and periodically re-evaluate my reservation value.
*   **L3: (Utility Awareness) Understand My Utility Function:** Be aware of my utility function, which defines the value of different outcomes.  Prioritize outcomes that provide higher utility.
*   **R1: (Initial Offer) Start High (But Reasonably):** Begin with an offer that is favorable to me, but not so outrageous that it immediately breaks down negotiation.  The initial offer influences the anchor for the negotiation.  Base the offer on my understanding of the other agent's potential utility.
*   **R2: (Concession Principle) Concede Gradually:** Make concessions slowly and deliberately. Each concession should be smaller than the previous one.
*   **L4: (Concession Analysis) Analyze Opponent Concessions:** Observe the pattern and magnitude of the opponent's concessions to infer their reservation value and strategy.
*   **R3: (Deadlines) Be Aware of Deadlines:** Understand any deadlines associated with the negotiation. Adjust my concession rate as the deadline approaches.
*   **L5: (Deadline Impact) Deadlines Increase Concessions:** Expect that both parties will increase their concession rate as the deadline approaches.

**II. Opponent Modeling and Prediction:**

*   **L6: (Opponent Observation) Track Opponent Offers:** Record all offers and concessions made by the opponent.
*   **L7: (Opponent Strategy Inference) Infer Opponent Strategy:**  Attempt to classify the opponent's negotiation strategy (e.g., Boulware, Conceder, TFT, Random) based on their behavior. Use machine learning models (e.g., Hidden Markov Models, Bayesian networks) for strategy inference.
*   **L8: (Opponent Utility Estimation) Estimate Opponent Utility Function:**  Infer the opponent's utility function based on their offers and concessions.  Consider using inverse reinforcement learning techniques.
*   **L9: (Opponent Reservation Value Prediction) Predict Opponent Reservation Value:**  Estimate the opponent's reservation value based on their behavior and available information. Use regression models or Kalman filtering.
*   **R4: (Strategy Adaptation) Adapt My Strategy to Opponent Strategy:** Adjust my negotiation strategy based on my understanding of the opponent's strategy and utility function.  If the opponent is a hard bargainer, be more persistent. If the opponent is a soft bargainer, be more assertive.
*   **L10: (Hidden Information) Recognize and Infer Hidden Information:**  The opponent may possess information that I do not.  Attempt to infer this hidden information from their behavior and public information.
*   **R5: (Information Revelation) Decide When to Reveal Information:** Strategically reveal information to influence the opponent's beliefs and behavior.  Consider revealing information that benefits both parties (to encourage cooperation).
*   **R6: (Counteroffer Strategy) Frame Counteroffers Effectively:**  Frame counteroffers in a way that highlights the benefits for the opponent.  Emphasize common ground and mutual gains.
*   **L11: (Pattern Recognition) Recognize Patterns in Opponent's Behavior:** Identify patterns in the opponent's behavior (e.g., predictable concession patterns, emotional responses) that can be exploited.

**III. Communication and Deception:**

*   **R7: (Communication Clarity) Communicate Clearly and Concisely:**  Use clear and unambiguous language to avoid misunderstandings.
*   **L12: (Intent Interpretation) Interpret Opponent Intent:**  Attempt to infer the opponent's underlying intentions from their communication. Be wary of deception.
*   **R8: (Deception Mitigation) Be Wary of Deception:**  Be aware that the opponent may be attempting to deceive me.  Cross-validate information and look for inconsistencies.
*   **L13: (Lie Detection) Detect Deception:** Learn to recognize verbal and nonverbal cues that may indicate deception. Use machine learning models to predict the likelihood of deception.
*   **R9: (Strategic Ambiguity) Use Strategic Ambiguity:**  In certain situations, it may be beneficial to be strategically ambiguous to avoid revealing information that could be exploited by the opponent.
*   **R10: (Commitments) Be Careful About Making Commitments:**  Think carefully before making commitments, as they can limit my flexibility.
*   **L14: (Commitment Detection) Detect Binding Commitments of Opponent:** Determine the strength of commitments made by opponent. Some commitments are easily broken.

**IV. Trust and Reputation:**

*   **L15: (Reputation Tracking) Track Opponent Reputation:**  Maintain a record of the opponent's past behavior and reputation.
*   **L16: (Trust Evaluation) Evaluate Opponent Trustworthiness:**  Assess the opponent's trustworthiness based on their reputation and past interactions.
*   **R11: (Building Trust) Act in a Trustworthy Manner:**  Be honest and reliable in my communication and actions to build trust with other agents.
*   **R12: (Punishing Defection) Punish Defection (Appropriately):** If the opponent defects (e.g., violates an agreement), take appropriate action to punish them. The punishment should be proportional to the offense. This encourages a future stable interaction with other agents as well.
*   **R13: (Forgiving) Balance Vengeance with Forgiveness:** Do not hold a grudge for long if they show signs of improving, as this might damage the collaboration long term.

**V. Risk Management and Exploration:**

*   **L17: (Risk Assessment) Assess the Risks of Different Negotiation Outcomes:**  Evaluate the potential risks and rewards associated with different negotiation outcomes.
*   **R14: (Risk Tolerance) Adjust My Risk Tolerance Based on Context:** Adjust my risk tolerance based on the specific situation. In high-stakes negotiations, be more risk-averse.
*   **R15: (Explore Alternatives) Explore Alternative Solutions:** Be creative and explore alternative solutions that may be mutually beneficial.
*   **L18: (Environmental Modeling) Understand the Environment:** Analyze the environmental constraints, such as power balance, availability of resources.

**VI. Learning and Adaptation:**

*   **L19: (Self-Reflection) Analyze My Own Performance:**  After each negotiation, analyze my own performance and identify areas for improvement.
*   **L20: (Learning from Experience) Learn from Past Experiences:**  Use machine learning techniques to learn from past experiences and improve my negotiation skills.  Employ experience replay for reinforcement learning agents.
*   **R16: (Experimentation) Experiment with Different Strategies:**  Experiment with different negotiation strategies to find what works best in different situations.
*   **R17: (Incremental Improvement) Continuously Improve My Skills:**  Strive for continuous improvement in my negotiation skills.
*   **L21: (Market Dynamics) Understand Overall Market Dynamics:** Be aware of the broader market dynamics, as market trends may affect negotiation strategy.
*   **R18: (Dynamic Strategy Update) Update Strategy Dynamically:** Adapt and change my negotiation strategy based on real time results and signals of the negotiations.

These learnings and rules, combined with the technical aspects and best practices outlined above, provide a strong foundation for developing effective multi-agent coordination systems with advanced negotiation protocols. The specific implementation will depend on the specific application and the capabilities of the agents. Regular evaluation and refinement are crucial for ensuring the success of the system.



## Automated Knowledge Ingestion (2026-02-05)
**Topic:** multi agent orchestration
Okay, let's analyze the concept of 'multi-agent orchestration' based on the aggregated data from Docs, GitHub, Stack Overflow, and Blogs, and structure the findings into a comprehensive markdown block.
    
```markdown
## Multi-Agent Orchestration: Comprehensive Analysis

This document aggregates knowledge from documentation, GitHub repositories, Stack Overflow discussions, and blog posts to provide a comprehensive overview of multi-agent orchestration.

### 1. CORE LEARNINGS: Key Concepts and Strategies

*   **Definition:** Multi-agent orchestration involves coordinating the actions of multiple autonomous agents to achieve a common, often complex, goal. It focuses on how these agents interact, collaborate, and resolve conflicts to operate effectively as a unified system.

*   **Key Concepts:**
    *   **Agent Autonomy:** Each agent operates independently, making decisions based on its own internal state, goals, and perception of the environment.
    *   **Communication:** Agents need to exchange information to coordinate their actions. This can be done through various mechanisms like message passing, shared blackboards, or knowledge representation languages.
    *   **Coordination Mechanisms:** These mechanisms facilitate collaboration and conflict resolution between agents. Examples include:
        *   **Contract Net Protocol:** Agents bid for tasks based on their capabilities.
        *   **Auctions:** Similar to contract nets, but with more formal bidding processes.
        *   **Voting:** Agents vote on which action to take.
        *   **Negotiation:** Agents engage in a dialogue to reach a mutually agreeable solution.
        *   **Planning and Scheduling:** Centrally plan and schedule actions for agents.
    *   **Environment:** The environment in which the agents operate provides context and feedback. Agents observe the environment to make decisions.
    *   **State Management:** Maintaining and synchronizing the state of the system, including agent states and environmental states.
    *   **Task Decomposition:** Breaking down complex goals into smaller, manageable tasks that can be assigned to individual agents.
    *   **Role Assignment:** Assigning specific roles and responsibilities to different agents based on their capabilities.
    *   **Conflict Resolution:** Resolving conflicts that arise when agents have competing goals or actions.
    *   **Resource Allocation:** Managing and allocating resources (e.g., computing power, data) to agents.
    *   **Monitoring and Adaptation:** Monitoring the performance of the multi-agent system and adapting the orchestration strategy as needed.
    *   **Fault Tolerance:** Designing the system to be resilient to agent failures.

*   **Strategies:**
    *   **Centralized Orchestration:** A single orchestrator agent manages the entire system. Simplifies coordination but can be a bottleneck.
    *   **Decentralized Orchestration:** Agents coordinate directly with each other. More robust but can be more complex to implement.
    *   **Hybrid Orchestration:** Combines centralized and decentralized approaches. Offers a balance between simplicity and robustness.
    *   **Hierarchical Orchestration:** Agents are organized in a hierarchy, with higher-level agents coordinating lower-level agents.
    *   **Emergent Behavior:** Design the system to encourage desirable emergent behavior from the interactions of individual agents.

### 2. OPERATIONAL RULES: Strict Guidelines for the Agent

These are general guidelines, and specific rules will heavily depend on the implementation and environment.

*   **Adherence to Assigned Roles:** Agents *must* operate within the defined boundaries of their assigned role and responsibilities. Deviations require explicit exceptions handled by the orchestration mechanism.

*   **Timely Communication:** Agents *must* communicate relevant information promptly and accurately to facilitate effective coordination. Delayed or inaccurate communication can disrupt the entire system.  Set timeouts on expected messages.

*   **Resource Constraints:** Agents *must* operate within the defined resource constraints (e.g., memory, CPU, network bandwidth). Exceeding these constraints can lead to instability and performance degradation.

*   **Conflict Resolution Protocol:** Agents *must* follow the established conflict resolution protocol when faced with conflicting goals or actions. Ignoring conflicts can lead to system failure.

*   **State Updates:** Agents *must* keep their internal state consistent with the overall system state. Inconsistent state can lead to incorrect decisions.

*   **Error Handling:** Agents *must* gracefully handle errors and exceptions. Unhandled errors can cause the agent to crash and disrupt the system.  Implement logging and reporting mechanisms.

*   **Security Protocols:** Agents *must* adhere to security protocols to protect sensitive data and prevent unauthorized access.

*   **Monitoring and Reporting:** Agents *must* actively monitor their own performance and report relevant metrics to the orchestration system.

*   **Compliance with Orchestration Directives:** Agents *must* comply with directives issued by the orchestrator or other coordinating agents.

*   **Context Awareness:** Agents *must* be aware of their current context and adapt their behavior accordingly. This includes understanding the current state of the environment, the goals of the system, and the actions of other agents.

### 3. CODE SYNTAX & EXAMPLES

These examples are illustrative and can be adapted to different programming languages and frameworks.  Python is often used for prototyping and experimentation.

**A. Python with LangChain and Agents (Illustrative Example)**

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
from langchain.utilities import SerpAPIWrapper

# Tool Definitions
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=OpenAI(temperature=0), verbose=True)

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    ),
]

# Initialize the Agent
llm = OpenAI(temperature=0) # Replace with your LLM provider

agent = initialize_agent(
    tools, llm, agent="zero-shot-react-description", verbose=True
)

# Run the Agent
query = "What is the current temperature in New York City in Celsius?  Then, what is that number divided by 2?"
result = agent.run(query)
print(result)
```

**Explanation:**

*   This example uses LangChain, a popular framework for building LLM-powered applications.
*   It defines two tools: a search tool and a calculator tool.
*   The `initialize_agent` function creates an agent that can use these tools to answer questions.  `zero-shot-react-description` is an example of an agent type that reasons about which tools to use at each step.
*   The `agent.run` method executes the agent with a given query.

**B. Example of Message Passing (Simplified)**

```python
import asyncio

async def agent1(queue1, queue2):
    """An example of a single agent receiving and sending messages"""
    while True:
        message = await queue1.get()
        print(f"Agent 1 received: {message}")
        await asyncio.sleep(1)
        await queue2.put(f"Message from Agent 1: {message}")

async def agent2(queue2, queue1):
    """Another agent processing messages from the queue."""
    while True:
        message = await queue2.get()
        print(f"Agent 2 received: {message}")
        await asyncio.sleep(1)
        await queue1.put(f"Message from Agent 2: {message}")

async def main():
    queue1 = asyncio.Queue()
    queue2 = asyncio.Queue()

    await queue1.put("Initial Message")

    agent1_task = asyncio.create_task(agent1(queue1, queue2))
    agent2_task = asyncio.create_task(agent2(queue2, queue1))

    await asyncio.sleep(5)  # Run for 5 seconds
    agent1_task.cancel()
    agent2_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
```

**Explanation:**

*   This example uses `asyncio` in Python to simulate message passing between two agents.
*   Each agent has its own queue for receiving messages.
*   Agents process messages from their queues and send responses to the other agent's queue.
*   This demonstrates a simple form of inter-agent communication.

**C. Configuration Example (YAML - Illustrative)**

```yaml
agents:
  - name: "TaskPlanner"
    type: "LLMAgent"
    llm: "openai-gpt-4" # Replace with model you like
    role: "Planner"
    tools: ["task_decomposition", "priority_assessment"]
    communication_channel: "task_queue"
  - name: "DataFetcher"
    type: "PythonAgent"
    module: "data_fetcher.py"
    class: "DataFetcherAgent"
    role: "Fetcher"
    tools: ["database_query", "api_call"]
    communication_channel: "task_queue"

orchestration:
  type: "centralized"
  coordinator: "TaskPlanner"
  conflict_resolution: "priority_based"
```

**Explanation:**

*   This YAML configuration file defines two agents: `TaskPlanner` and `DataFetcher`.
*   It specifies the type, role, tools, and communication channels for each agent.
*   It also defines the orchestration type (centralized) and the conflict resolution strategy.

**D.  Function Signature Example (Illustrative)**

```python
def coordinate_agents(agents: List[Agent], environment: Environment, objective: str) -> List[Action]:
    """
    Coordinates the actions of multiple agents to achieve a given objective.

    Args:
        agents: A list of agent objects.
        environment: An environment object that represents the current state of the environment.
        objective: A string representing the overall objective of the multi-agent system.

    Returns:
        A list of action objects, representing the actions that each agent should take.
    """
    # Implementation details would go here...
    pass
```

**Explanation:**

*   This function signature illustrates a common pattern for coordinating agents.
*   It takes a list of agents, an environment object, and an objective as input.
*   It returns a list of actions that each agent should take.

**Important Considerations:**

*   **Scalability:** Design the orchestration system to handle a large number of agents.
*   **Security:** Implement security measures to protect the system from malicious attacks.
*   **Observability:**  Implement logging and monitoring to track the performance of the system and identify potential issues.
*   **Reproducibility:** Use version control and configuration management to ensure that the system can be easily reproduced.

This structured markdown block provides a comprehensive overview of multi-agent orchestration, covering key concepts, operational rules, and code examples. Remember that the specific implementation details will vary depending on the application and the chosen framework.
```


## Automated Knowledge Ingestion (2026-02-10)
**Topic:** gmail automation
```markdown
## Gmail Automation: Core Learnings, Operational Rules, and Code Examples

This document aggregates data from various sources (Docs, GitHub, Stack Overflow, Blogs) to provide a comprehensive overview of Gmail automation.

### 1. CORE LEARNINGS: Key Concepts and Strategies

*   **Gmail API vs. IMAP/SMTP:**
    *   **Gmail API:**  Recommended for most automation tasks, especially for modern applications. Offers granular control, OAuth 2.0 authentication, and access to advanced features like message threading and labels.  Requires enabling the API and creating credentials in the Google Cloud Console.
    *   **IMAP/SMTP:**  Suitable for basic tasks like sending and receiving emails using standard protocols. Simpler to set up initially but offers less control and may trigger security warnings if not configured correctly with app passwords or less secure app access.  Becoming increasingly difficult to rely on as Gmail tightens security around password-based authentication.

*   **OAuth 2.0 Authentication:** Essential for using the Gmail API securely.  Involves obtaining user consent through a browser-based flow and storing refresh tokens for long-term access.  Consider using a library like `google-auth` in Python or a similar library in other languages to handle OAuth flow.

*   **Message Formatting (MIME):**  Understanding MIME types is crucial for creating complex emails with attachments, HTML content, and embedded images.  Use appropriate libraries (e.g., `email.mime` in Python) to construct MIME messages correctly.

*   **Handling Rate Limits:** The Gmail API has usage limits. Implement strategies to avoid exceeding these limits, such as:
    *   **Batching requests:**  Combine multiple operations into a single API call where possible.
    *   **Using exponential backoff:**  If a request fails due to rate limiting, wait for a short period and retry.  Increase the waiting time exponentially with each subsequent retry.
    *   **Monitoring usage:** Track your API usage to identify potential bottlenecks.

*   **Searching for Emails:** The Gmail API provides a powerful search functionality using `users.messages.list`.  Learn to construct effective search queries using operators like `from:`, `to:`, `subject:`, `after:`, `before:`, `label:`, and `in:`.

*   **Labels and Threads:** Leverage Gmail's labeling and threading capabilities to organize and manage emails effectively. Understand how to apply labels, move emails between threads, and retrieve thread information.

*   **Error Handling:** Implement robust error handling to gracefully handle unexpected situations, such as authentication failures, API errors, and network issues.  Log errors for debugging and monitoring.

*   **Security Best Practices:** Store credentials securely, avoid hardcoding sensitive information in code, and regularly review and update your automation scripts. Never expose API keys publicly.

### 2. OPERATIONAL RULES: Strict Guidelines for the Agent

*   **Authentication is Mandatory:** Always authenticate using OAuth 2.0 or an equally secure method. Avoid insecure authentication methods.
*   **Respect User Privacy:**  Handle email data with utmost care and respect user privacy.  Never store or share sensitive information unnecessarily. Adhere to GDPR and other relevant privacy regulations.
*   **Adhere to Gmail API Usage Limits:**  Implement rate limiting and backoff strategies to avoid exceeding API quotas. Monitor API usage regularly.
*   **Error Logging:**  Log all errors and exceptions to facilitate debugging and monitoring.  Include relevant information, such as timestamps, error messages, and API request details.
*   **Secure Credential Storage:** Store API keys and refresh tokens securely, using environment variables, configuration files, or dedicated secret management tools.  Never hardcode credentials in code.
*   **Minimize Data Usage:** Only retrieve the necessary email data to minimize resource consumption and improve performance.
*   **Code Reviews:**  All automation scripts should undergo thorough code reviews to identify potential security vulnerabilities, bugs, and performance issues.
*   **Regular Updates:** Keep the automation scripts and libraries up-to-date to benefit from security patches, bug fixes, and performance improvements.
*   **Avoid Sending Spam:** Refrain from sending unsolicited emails or engaging in spamming activities.  Comply with Gmail's anti-spam policies.
*   **Handle Attachments Carefully:** Sanitize and validate attachments to prevent security risks, such as malware infections.  Limit the size and type of attachments that are processed.
*   **User Consent:**  If automating on behalf of a user, explicitly obtain their consent and provide a clear explanation of the automation process.

### 3. CODE SYNTAX & EXAMPLES:

#### Python (using Google API Client Library)

```python
from googleapiclient.discovery import build
from google.oauth2 import credentials
from email.mime.text import MIMEText
import base64

# Replace with your refresh token, client ID, and client secret
SCOPES = ['https://mail.google.com/']

def get_gmail_service(refresh_token, client_id, client_secret):
    """Authenticates with Gmail API and returns a service object."""
    creds = credentials.Credentials.from_authorized_user_info(
        info={
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret,
            'token_uri': 'https://oauth2.googleapis.com/token'
        },
        scopes=SCOPES
    )
    return build('gmail', 'v1', credentials=creds)


def search_emails(service, query):
    """Searches for emails matching the specified query."""
    try:
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        return messages
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_email(service, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()

    # Decode from Base64
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    return msg_str  #Raw email content
  except Exception as e:
    print(f"An error occurred: {e}")
    return None



def send_email(service, sender, to, subject, message_text):
    """Sends an email."""
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8")).decode("utf-8")
    try:
        send_message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        print(f"Message Id: {send_message['id']}")
        return send_message
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == '__main__':
    # Replace with your actual credentials and email addresses
    REFRESH_TOKEN = "YOUR_REFRESH_TOKEN"
    CLIENT_ID = "YOUR_CLIENT_ID"
    CLIENT_SECRET = "YOUR_CLIENT_SECRET"
    SENDER_EMAIL = "your_email@gmail.com"
    RECIPIENT_EMAIL = "recipient_email@example.com"

    service = get_gmail_service(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)

    # Search for emails with specific subject
    search_query = "subject:Important Update"
    messages = search_emails(service, search_query)

    if messages:
        print(f"Found {len(messages)} messages matching the query.")
        #Retrieve and print the raw content of the first email
        raw_email_content = get_email(service, messages[0]['id'])
        if raw_email_content:
          print(f"Raw Email Content:\n{raw_email_content.decode()}") # decode() to view readable text

    else:
        print("No messages found matching the query.")

    # Send an email
    subject = "Automated Email"
    message_text = "This is an automated email sent using the Gmail API."
    send_email(service, SENDER_EMAIL, RECIPIENT_EMAIL, subject, message_text)
```

#### Function Signatures (Gmail API - Python)

*   `googleapiclient.discovery.build(serviceName, version, credentials=None)`:  Creates a service object for interacting with the Gmail API.
*   `gmail.users().messages().list(userId='me', q='search_query')`: Lists messages matching a search query.  Returns a dictionary containing a `messages` list (each element with an `id`).
*   `gmail.users().messages().get(userId='me', id='message_id', format='raw')`: Retrieves a specific message by its ID. The `format='raw'` argument retrieves the entire message as a MIME-encoded string.
*   `gmail.users().messages().send(userId='me', body={'raw': 'base64_encoded_message'})`:  Sends an email.  The email body must be base64-encoded and URL-safe.

#### Search Query Examples (Gmail API)

*   `from:sender@example.com`:  Emails from a specific sender.
*   `to:recipient@example.com`:  Emails to a specific recipient.
*   `subject:Meeting`:  Emails with a specific subject.
*   `after:2023/01/01`:  Emails received after a specific date.
*   `before:2023/01/31`:  Emails received before a specific date.
*   `label:important`:  Emails with a specific label.
*   `in:inbox`:  Emails in the inbox.
*   `has:attachment`: Emails with attachments.
*   `is:unread`: Unread emails.
*   `from:sender@example.com subject:"Important Update"`: Combining multiple search criteria.

#### Common Errors and Solutions

*   **`googleapiclient.errors.HttpError: <HttpError 403 when requesting https://gmail.googleapis.com/gmail/v1/users/me/messages?alt=json&q=... returned "User Rate Limit Exceeded. Rate of requests for user exceed configured project quota. Expected available per-user quota: 100.0. Actual available per-user quota: 0.0 for this user.">`**  Solution: Implement exponential backoff and batch requests to reduce the rate of API calls.

*   **`oauth2client.client.AccessTokenRefreshError: invalid_grant`**  Solution:  The refresh token might be invalid or revoked.  Re-authenticate the user and obtain a new refresh token. Ensure the client ID and secret are correct.  Sometimes caused by the Google Account being disconnected from the application.

*   **`ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` (when using IMAP/SMTP)** Solution: This is often due to outdated certificate bundles on your system.  Try updating your `certifi` package (e.g., `pip install --upgrade certifi`). Consider using more modern OAuth2 flow instead of relying solely on username/password authentication.

This structured document provides a solid foundation for understanding and implementing Gmail automation.  Remember to prioritize security, error handling, and adherence to API usage limits for a robust and reliable automation solution.
```

