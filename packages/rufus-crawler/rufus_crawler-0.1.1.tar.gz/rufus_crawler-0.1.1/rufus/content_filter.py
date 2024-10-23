# rufus/content_filter.py
import openai
import json

class ContentFilter:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def filter_content(self, instruction, crawled_data):
        filtered_data = []
        
        for entry in crawled_data:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Keep data only useful for {instruction}. Content: {entry['content']}"}
                    ]
                )
                relevant_content = response.choices[0].message['content']
                filtered_data.append({"URL": entry["URL"], "content": relevant_content})
            except Exception as e:
                print(f"Error filtering content from {entry['URL']}: {e}")
        
        return filtered_data

    def save_filtered_data(self, filtered_data, output_file="output.json"):
        with open(output_file, "w") as f:
            json.dump(filtered_data, f, indent=4)
        print(f"Filtered content saved to '{output_file}'")
