import os
import xml.etree.ElementTree as ET
import logging

source_dir = "Data"
output_dir = os.path.join(source_dir, "modified")
log_dir = os.path.join(source_dir, "logs")
log_file = os.path.join(log_dir, "process.log")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

if not os.path.exists(source_dir):
    logging.error(f"Folder '{source_dir}' tidak ditemukan!")
    print(f"Error: Folder '{source_dir}' tidak ditemukan!")
    exit(1)

for filename in os.listdir(source_dir):
    if filename.endswith(".xml"):
        file_path = os.path.join(source_dir, filename)
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            for jvnumber in root.findall(".//JVNUMBER"):
                if jvnumber.text and jvnumber.text.isdigit():
                    jvnumber.text = jvnumber.text.zfill(len(jvnumber.text) + 3)
                else:
                    logging.warning(f"JVNUMBER tidak valid di {filename}: {jvnumber.text}")

            output_path = os.path.join(output_dir, filename)
            tree.write(output_path, encoding="utf-8", xml_declaration=True)
            
            print(f"Sukses: {filename} → {output_path}")
            logging.info(f"Sukses memproses {filename} → {output_path}")

        except ET.ParseError as e:
            logging.error(f"Error parsing XML {filename}: {e}")
        except Exception as e:
            logging.error(f"Error saat memproses {filename}: {e}")

print("\nProses selesai! Semua file telah disimpan di folder 'modified'.")
print("\nProses selesai! Semua file telah disimpan di folder 'modified'.")
print("\nProses selesai! Semua file telah disimpan di folder 'modified'.")
