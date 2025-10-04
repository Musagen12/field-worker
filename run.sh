#!/bin/bash
# ===============================
# Full project setup script
# ===============================

# Exit immediately if any command fails
set -e

# Ensure python3.12-venv is installed first
echo "🔧 Installing python3.12-venv if not present..."
apt install -y python3.12-venv

# -------------------------------
# Step 1: Backend setup
# -------------------------------
cd backend || { echo "❌ backend folder not found"; exit 1; }

echo "=== Setting up Python environment ==="
# Create venv if it doesn’t exist
if [ ! -d "venv" ]; then
    python3.12 -m venv venv
    echo "✅ Virtual environment created."
fi

# Activate environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "✅ Environment activated."
else
    echo "❌ venv/bin/activate not found. Virtual environment setup failed!"
    exit 1
fi

# Install backend dependencies
if [ -f "requirements.txt" ]; then
    echo "📦 Installing backend dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "❌ requirements.txt not found!"
    exit 1
fi

# Run backend server in background
echo "🚀 Starting backend server..."
nohup uvicorn main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1 &
BACKEND_PID=$!
echo "✅ Backend running (PID: $BACKEND_PID)"

# Wait 10 seconds for server and database to initialize
echo "⏳ Waiting 10 seconds for backend to initialize..."
sleep 10

# Seed admin
if [ -f "seed_admin.py" ]; then
    echo "🌱 Seeding admin user..."
    python3 seed_admin.py
else
    echo "⚠️ No seed_admin.py file found, skipping admin seeding."
fi

# -------------------------------
# 2️⃣ Frontend setup
# -------------------------------
cd ../task-dispatch-pro || { echo "❌ frontend folder not found"; exit 1; }

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️ Node.js not found. Installing..."
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt install -y nodejs
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "⚠️ npm not found. Installing..."
    sudo apt install -y npm
fi

echo "✅ Node.js and npm are installed."
echo "Node.js: $(node -v), npm: $(npm -v)"

echo "=== Setting up frontend ==="
npm install

# Run frontend dev server
echo "🚀 Starting frontend dev server..."
npm run dev &
FRONTEND_PID=$!
echo "✅ Frontend running (PID: $FRONTEND_PID)"
