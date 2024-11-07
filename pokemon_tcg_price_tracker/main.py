# Import required libraries
import os
from supabase import create_client, Client
import openai

# Set up Supabase client with environment variables
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Function to get embedding vector for a question using OpenAI
def get_question_embedding(question):
    response = openai.embeddings.create(input=question, model="text-embedding-3-small")
    return response.data[0].embedding

# Function to get relevant Pokemon card context based on the question
def get_context(question) -> str:
    # Get embedding for the question
    question_embedding = get_question_embedding(question)
    results = []
    # Query Supabase for related cards using vector similarity
    # Remember to create the function find_related_cards in supabase
    query = supabase.rpc("find_related_cards",{'question_vector': question_embedding}).execute()
    # Process query results
    for item in query.data:
        card_metadata = item;
        results.append(card_metadata)
    return results

# Function to get AI response using OpenAI's chat completion
def get_response(question: str):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about Pokemon cards. Use only the provided context to answer questions. If the information isn't in the context, say so."},
            {"role": "user", "content": f"Question: {question}\n\nContext:\n{get_context(question)}"}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Example usage
question = "show me cards that are selling for more than $100"
answer = get_response(question)
print("Answer:", answer)