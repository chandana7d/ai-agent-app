
from translator import QueryTranslator
from router import QueryRouter
from retriever import QueryRetriever
from generator import QueryGenerator 
from indexer import ChromaVectorStore
# from crawler import GitHubCrawler
# from indexer import DocumentIndexer

GITDATA_QUESTIONS  = [
    "What is the primary capability of the Heroku platform?",
    "How does Heroku's abstraction differ from traditional PaaS solutions like Heroku?",
    "What are some examples of cloud services that users can directly operate on with Heroku?",
    "Which security concepts are typically hidden from end users in Heroku?",
    "How does Heroku handle direct changes made by administrators on the cloud account?",
    "What is the most fundamental construct in Heroku?",
    "How does a Tenant relate to infrastructure in Heroku?",
    "What are the four fundamental aspects of a Tenant in Heroku?",
    "How does Heroku implement security boundaries between Tenants?",
    "How does Heroku facilitate user access control at the Tenant level?",
    "How does Heroku support billing segregation?",
    "What is a common use case for Tenants in an organization using Heroku?",
    "What are the two preexisting Tenants in Heroku?",
    "What is the purpose of the Default Tenant in Heroku?",
    "How does the Compliance Tenant differ from other Tenants?",
    "How can users configure settings to apply to all new Tenants under a Plan?",
    "Where in the Heroku portal can you add Tenant Config settings?",
    "What is the significance of the 'TenantConfig' Config Type?",
    "How can users verify that Tenant Config settings are enabled for new Tenants?",
    "What is the relationship between Plans and Tenant Config settings?",
    "Can Tenant Config settings be applied retroactively to existing Tenants?",
    "How does Heroku handle inter-tenant communication?",
    "What role do Security Groups play in Tenant isolation?",
    "How does Heroku leverage cloud-specific concepts like IAM roles and Managed Identities?",
    "What is the significance of KMS keys in Heroku's Tenant model?",
    "How does Heroku handle resource termination when a Tenant is deleted?",
    "Can users have access to multiple Tenants, and how is this managed?",
    "How does Heroku's Tenant model support different environments like Dev, QA, and Prod?",
    "What is the purpose of tagging resources with the Tenant's name in the cloud provider?",
    "How does Heroku's abstraction model benefit developers without DevOps expertise?"
]


NON_DOC_QUESTIONS = [
    "What are Heroku's main competitors in the DevOps automation market?",
    "How does Heroku's pricing model compare to other DevOps platforms?", 
    "What is the total funding raised by Heroku to date?",
    "Who are the founders of Heroku and what is their background?",
    "What specific industries or sectors does Heroku primarily serve?",
    "How many employees does Heroku currently have?",
    "What partnerships or integrations does Heroku have with other tech companies?",
    "What is Heroku's market share in the DevOps automation industry?",
    "Has Heroku won any industry awards or recognitions?",
    "What is the customer retention rate for Heroku's services?"
]


def run_pipeline(query):
    vector_store = ChromaVectorStore().get_vectorstore()

    user_query        = QueryTranslator().invoke(query=query)

    r_decision        = QueryRouter(vector_store=vector_store).invoke(query=user_query)
    context           = QueryRetriever().invoke(router_decision=r_decision)
    user_output       = QueryGenerator().invoke(context=context)

    return r_decision, context, user_output

for query in GITDATA_QUESTIONS:
    print("------------------------------------------------------------------------------------------")
    print(">>> User Question : ", query)
    r_decision, context, user_output = run_pipeline(query=query)
    #print(">>> ", r_decision.is_vectordb, r_decision.tool_name , len(context.docs) if context.docs is not None else 0  )
    print(f">>> {user_output.content}")

#TEST_QUERY = ["What is the customer retention rate for 's services?"]

# for query in NON_DOC_QUESTIONS:

#     print("------------------------------------------------------------------------------------------")
#     print(">>> User Question : ", query)
#     r_decision, context, user_output = run_pipeline(query=query)
#     #print(">>> ", r_decision.is_vectordb, r_decision.tool_name , len(context.docs) if context.docs is not None else 0  )
#     print(f">>> {user_output.content}")


# TEMP_QUESTION = ["what is the weather in Seattle?","what is the weather in New York?","what is the weather in SF"]

# for query in TEMP_QUESTION:

#     print("------------------------------------------------------------------------------------------")
#     print(">>> User Question : ", query)
#     r_decision, context, user_output = run_pipeline(query=query)
#     print(">>> ", r_decision.is_vectordb, r_decision.tool_name , len(context.docs) if context.docs is not None else 0  )
#     print(f">>> {user_output.content}")





