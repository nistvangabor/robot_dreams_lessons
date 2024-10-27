class CSVExporter:
    def export(self, data):
        print("Exporting data to CSV format")
        # Logic to export data as CSV
        # This is just a simplified example print statement

class JSONExporter:
    def export(self, data):
        print("Exporting data to JSON format")
        # Logic to export data as JSON

class XMLExporter:
    def export(self, data):
        print("Exporting data to XML format")
        # Logic to export data as XML

def export_data(exporter, data):
    # Using duck typing: only cares that the exporter has an 'export' method
    exporter.export(data)

# Usage
data = {"name": "Alice", "age": 30}

csv_exporter = CSVExporter()
json_exporter = JSONExporter()
xml_exporter = XMLExporter()

export_data(csv_exporter, data)  # Output: Exporting data to CSV format
export_data(json_exporter, data)  # Output: Exporting data to JSON format
export_data(xml_exporter, data)   # Output: Exporting data to XML format