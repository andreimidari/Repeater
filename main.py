import sys
import os

parent_folder = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(parent_folder, "Lib"))

from flowlauncher import FlowLauncher
class Repeater(FlowLauncher):

    def query(self, query):
        results = []

        if '::' not in query:
            results.append({
                "Title": "Repeater: How to use",
                "SubTitle": "Format: <number>::<text to repeat>",
                "IcoPath": "app.png"
            })
            return results

        parts = query.split('::', 1)

        if len(parts) != 2:
            results.append({
                "Title": "Invalid Format",
                "SubTitle": "Please use the format: <number>::<text>",
                "IcoPath": "app.png"
            })
            return results

        num_str, text_to_repeat = parts

        if not text_to_repeat:
            results.append({
                "Title": "Text is empty",
                "SubTitle": "Please provide some text after '::' to repeat.",
                "IcoPath": "app.png"
            })
            return results

        try:
            repeat_count = int(num_str.strip())
            if repeat_count <= 0:
                results.append({
                    "Title": "Number must be positive",
                    "SubTitle": f"'{num_str.strip()}' is not a positive number.",
                    "IcoPath": "app.png"
                })
                return results
        except ValueError:
            results.append({
                "Title": "Invalid Number",
                "SubTitle": f"'{num_str.strip()}' is not a valid integer.",
                "IcoPath": "app.png"
            })
            return results

        repeated_text = text_to_repeat * repeat_count

        results.append({
            "Title": f"Result: {repeated_text}",
            "SubTitle": "Select this item to copy the result to your clipboard",
            "IcoPath": "app.png",
            "JsonRPCAction": {
                # This action copies the text to the clipboard when the user selects the result.
                "method": "Flow.Launcher.CopyToClipboard",
                "parameters": [repeated_text]
            }
        })

        return results

if __name__ == "__main__":
    Repeater()

