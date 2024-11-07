# Pokemon TCG Card Price Tracker

This application helps users query and analyze Pokemon card prices using embeddings and AI-powered search. It connects to a database of Pokemon cards and provides intelligent responses about card prices and market trends.

## Features

- AI-powered natural language querying of Pokemon card data
- Real-time price comparisons between regular and reverse holo cards
- Integration with TCGPlayer and Cardmarket pricing data
- Vector similarity search using embeddings
- GPT-4 powered responses for complex card-related questions

## Prerequisites

- Python 3.8+ - [Download Python](https://www.python.org/downloads/)
- OpenAI API key - [Get API Key](https://platform.openai.com/api-keys)
- Supabase account and project - [Sign Up](https://supabase.com/)
- Vector extension enabled in Supabase - [pgvector Setup Guide](https://supabase.com/docs/guides/database/extensions/pgvector)
- Airbyte Cloud account - [Sign Up](https://airbyte.com/)
- Pokemon TCG API key - [Developer Portal](https://dev.pokemontcg.io/)

## Required Environment Variables

```bash
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_key
export OPENAI_API_KEY=your_openai_api_key
```

## Installation

1. Clone the repository


2. Install dependencies

```bash
pip install -r requirements.txt
```


## Usage
1. Write your question in the question variable in main.py
2. Run the script

```bash
python3 main.py
```

The application will:
1. Convert your question into an embedding
2. Search the database for relevant cards via the find_related_cards function in Supabase
3. Return detailed pricing information including:
   - Card ID and name
   - Rarity
   - TCGPlayer market prices
   - 30-day average prices
   - Direct links to purchase

## Database Schema

The application expects a PostgreSQL database in Supabase with a `cards` table containing:
- Card metadata (JSON)
- Card embeddings (vector)
- Price information
- Market data from multiple sources
- vector extension enabled

## Contributing

Feel free to open issues or submit pull requests with improvements.
