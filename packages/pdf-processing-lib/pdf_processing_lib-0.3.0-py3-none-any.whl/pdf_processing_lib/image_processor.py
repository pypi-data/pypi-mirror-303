import os
import pandas as pd
from ultralytics import YOLO
import gc
import time

class ImageProcessor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        if self.model is None:
            self.model = YOLO(self.model_path)

    def process_batch(self, image_batch, output_folder):
        self.load_model()  # Ensure model is loaded
        results = self.model(image_batch, conf=0.12)  # Process the entire batch at once
        
        for img_path, result in zip(image_batch, results):
            boxes = result.boxes.xyxy.cpu().numpy()
            class_ids = result.boxes.cls.cpu().numpy()
            confidences = result.boxes.conf.cpu().tolist()
            names = result.names
            
            data = []
            for box, class_id, confidence in zip(boxes, class_ids, confidences):
                x1, y1, x2, y2 = box
                class_id = int(class_id)
                class_name = names[class_id]
                data.append([x1, y1, x2, y2, confidence, class_id, class_name])
            
            df = pd.DataFrame(data, columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class_id', 'class_name'])
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            output_path = os.path.join(output_folder, f'{base_name}.tsv')
            df.to_csv(output_path, sep='\t', index=False)

            # Clear memory for this iteration
            del boxes, class_ids, confidences, data, df
        
        # Clear batch results
        del results
        gc.collect()

    def process_images_in_output_folder(self, output_folder):
        image_folder = os.path.join(output_folder, f"{os.path.basename(output_folder[:-7])}_images")
        if os.path.exists(image_folder):
            results_yolo_folder = os.path.join(output_folder, "results_yolo")
            os.makedirs(results_yolo_folder, exist_ok=True)
            image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and f.lower().endswith('.jpg')]
            
            start_time = time.time()
            batch_size = 10  # Adjusted for CPU processing

            for i in range(0, len(image_files), batch_size):
                batch = image_files[i:i+batch_size]
                self.process_batch(batch, results_yolo_folder)
                
                # Clear memory after each batch
                gc.collect()

            end_time = time.time()
            return len(image_files), end_time - start_time
        return 0, 0

    def process_directory(self, input_directory):
        total_images_processed = 0
        total_time_spent = 0.0
        for entry in os.listdir(input_directory):
            path = os.path.join(input_directory, entry)
            if os.path.isdir(path) and path.endswith('_output'):
                images_processed, time_spent = self.process_images_in_output_folder(path)
                total_images_processed += images_processed
                total_time_spent += time_spent
        avg_time_per_image = total_time_spent / total_images_processed if total_images_processed > 0 else 0
        print(f"Total JPEG images processed: {total_images_processed}")
        print(f"Total processing time: {total_time_spent:.2f} seconds.")
        print(f"Average time per JPEG image: {avg_time_per_image:.2f} seconds.")
        return total_images_processed, total_time_spent, avg_time_per_image