import pandas as pd
from datetime import datetime, timedelta

# Define the CSV file for tracking watering history
history_file = 'watering_history.csv'

# Define thresholds and parameters
MOISTURE_THRESHOLD = 30  # below this value, watering is needed
MAX_DAILY_WATER_AMOUNT = 1000  # maximum amount of water recommended per day (in ml)
RECENT_WATERING_PERIOD = timedelta(days=1)  # recent watering period (e.g., last 24 hours)
MOISTURE_JUMP_THRESHOLD = 600
# Initialize previous moisture value
previous_moisture_level = None

def log_watering(amount):
    if amount > 0:
        now = datetime.now()
        log_entry = {
            'timestamp': now,
            'amount': amount
        }
        
        # Create a DataFrame with the new entry
        df_entry = pd.DataFrame([log_entry])
        
        # Append to the CSV file, creating it if it doesn't exist
        if not pd.io.common.file_exists(history_file):
            df_entry.to_csv(history_file, index=False)
        else:
            df_entry.to_csv(history_file, mode='a', header=False, index=False)
        print(f"Watering event logged: {amount} ml at {now}")
    else:
        print("No watering event recorded. Amount must be greater than zero.")

def read_watering_history():
    """Read watering history from a CSV file."""
    try:
        df = pd.read_csv(history_file)
        if 'timestamp' in df.columns and 'amount' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            return df
        else:
            print("Required columns are missing from the file")
            return pd.DataFrame(columns=['timestamp', 'amount'])
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame(columns=['timestamp', 'amount'])
    
def get_last_watering_time(df):
    """Get the timestamp of the last watering event."""
    if not df.empty:
        return df['timestamp'].max()
    return None

def total_water_today():
    """Calculate the total amount of water received today."""
    now = datetime.now()
    today = now.date()
    
    # Read the CSV file
    try:
        df = pd.read_csv(history_file)
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Filter rows for today
        today_data = df[df['timestamp'].dt.date == today]
        
        # Calculate the total water amount
        total_amount = today_data['amount'].sum()
        return total_amount
    except FileNotFoundError:
        return 0
    
def detect_watering(current_moisture_level):
    """Detect if watering has occurred based on a jump in moisture level."""
    global previous_moisture_level
    if previous_moisture_level is not None and current_moisture_level > MOISTURE_JUMP_THRESHOLD and previous_moisture_level <= MOISTURE_JUMP_THRESHOLD:
        log_watering(current_moisture_level - previous_moisture_level)  # log the change in moisture level
    # Update previous moisture level
    previous_moisture_level = current_moisture_level

def suggest_watering(current_moisture_level):
    """Suggest whether to water now or later based on current moisture level and history."""
    # Get historical watering data
    watering_history_df = read_watering_history()
    last_watering_time = get_last_watering_time(watering_history_df)
    water_today = total_water_today()

    # Determine if current moisture level is below threshold
    if current_moisture_level < MOISTURE_THRESHOLD:
        if last_watering_time is None or datetime.now() - last_watering_time > RECENT_WATERING_PERIOD:
            if water_today < MAX_DAILY_WATER_AMOUNT:
                return "Water the plant now"
            else:
                return "Consider watering later; you have already given enough water today"
        else:
            return "Watering later might be sufficient; recent watering detected"
    else:
        return "No watering needed"

# Example usage
current_moisture_level = 25  # replace this with actual sensor reading
#log_watering(5)

suggestion = suggest_watering(current_moisture_level)
#print("Watering Suggestion:", suggestion)