import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
import json

# Url = https://docs.google.com/spreadsheets/d/1vgn2iIzyGwhX1hPgNO7p6O2GPUFapjwQIpC8p2a7Z68/edit?usp=sharing

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

cd = {
  "type": "service_account",
  "project_id": "webjdm-424905",
  "private_key_id": "30687d2e3b9b0b5220b2f3ebdcea2f60628fbb10",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCS+cshHuYv3nLt\nUMH7IlkI5/vW+9+MmwFf/b9fvGAZEtnG4Cfd0lhgHptf6yVMxe6yJ8nmz6e2TnbA\nvZLuhjlHFwMVv+3yBZ+STlsucxKOEKtQaSJO0aM90dYSQD0tKehUMReTKvJJ85G6\nvH24xSIxVeDwiypJ3k7i82llqxBsk8CELjmawOifrJn7FaKWqj2V+n+RYcITgegd\nny2MVyoNliyMiNxjPuqRoJhH2jWP+i5MoFKyR8WBefWHIn8dSvK70xak+9ksoOB9\nDft5o+SD0aChM0+ZZudvqpfhdxNYNlX2Q6bDIRhHCN9TwxJ3j3cDDL0Lp/ZcIpuq\nZ1JAG1jNAgMBAAECggEAHIEmGFsUBRIlI2nvaRuA/YVyVgA825nfUyTVBgX0dEBv\n7I5iJPbrzV56P0jNT92uXK5zTZiV2/lNNjW+BpURDDzGDCSQSwk0qK0aKYDHRzar\n5vkw3mzxdiaZWCpNwxHW3Wc0/YWNfnKm33q5fkl7R2qyqKwwzCk5jvHqzb02vvvA\nh1QtUgl24KyK6C6r8Sw9NuRUO1VSz2q/05Ez9+4s0p7J7dao73hLxx+QauNJM/kO\n+H46e8YbaERtc9ZA6AQt5NNEUcYiPnQ2Lnl+SxahIDYjYtMQoD5zv+2L0KOKE4hP\nrxF9fEzbRyTgDTkOx8BdeoII1Sg0ljm9t9uUJm2pGQKBgQDJIIY2B37JSDTYuNvR\ni52yXOvDhE+Zz+jZ3d/DCw+cHDmUfroS30UtYONioKw/cD8SsEBXq7PLZID/Y5bs\nCxDQjVmyTDrI6HlL6luvH3r/23zHe8aSuwBxNIF+eqAZoJP8FQzFj321OF+bZz0v\nLz+EmKdKhIduyXf++0l0FatlNQKBgQC7EyM63RXS0ob5mrHQw6ozmIlBlYgZ9X0v\ndJzgzoxlqNIh0ofEy3ot/jFeRM+ML5ti9chog2qjdo8YQ0icL0i7kSNFLWVlOu+U\neoiXJ7FClEuxK/EBlZpubcT8xv3qB+jH1Ub2HM5pfMKWxyTKvTv1CVm+VeaxtbIM\n4j/PiHSQOQKBgBrtNcqp+jlsZ1bUeOl27afhdNb6McX/5ca1Q63TH0XhKXxN8w9v\nwM0weYDMzgK4Pll8K0ERhcKnM/X9GUmEub2SDv4l4oDfTs3xFFE/v7HdarkyQwWF\n76s4QlXyiNilfOp0zv7sFQJcB8DAc5qLks9nuI3rbE5SvrPuZIkcFZQ5AoGAHOnD\nSyi6Y8AYDmHjU6G6H4lWxWUoCOMROxFp4bDqsBecio+wXjEYrB0aYjh+X2tIN85G\n8ChHhgYf7Z8QjNseAadX7Swr/K5UMv2RONNwqRqkbDifYiBOIv0iMfNLcS1Rw/jp\no8Yl/NXEeWtD+3Wt25xbW3iJVDQB1c3uENRFN7kCgYBdz7bY+bPGoJl8g6M1uyWh\nB9q0sQP/mWmVK5c+J1zA6q2+T9ClvjqTycKmeJ4Sa9M/ZZhOEHmXG87/1dkejr2h\nxm42NjLo0tlZirAe5eZje+Ip08ce5LipVjrZuoYzA3by8tYXI4RLAsJ2bIGwo+iz\njU5HhmB07cRUXCvGwFOEMQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "streamlit-gsheet@webjdm-424905.iam.gserviceaccount.com",
  "client_id": "100005646824935102507",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/streamlit-gsheet%40webjdm-424905.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

with open('credentials.json', 'w') as outfile:
  json.dump(cd, outfile)
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1vgn2iIzyGwhX1hPgNO7p6O2GPUFapjwQIpC8p2a7Z68").sheet1

existing_data = sheet.get_all_values()
print(existing_data)
data_list = []
for row in existing_data:
    data_list.append({
        'Name': row[0],
        'Family': row[1]
    })
existing_df = pd.DataFrame(data_list)
st.write(existing_df)

# ---------------------------------------------------
new_name = st.text_input("Enter Name:")
new_family = st.text_input("Enter Family:")
if st.button("Insert"):
    new_row = [new_name, new_family]
    sheet.append_row(new_row)
    st.write("Data inserted successfully!")