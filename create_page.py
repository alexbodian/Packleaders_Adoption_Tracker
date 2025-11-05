def main():
    # retrieve_api()
    # Load environment variables
    load_dotenv()
    
    # Get and validate spreadsheet ID
    spreadsheet_id = os.getenv("spreadsheet_id")



if __name__ == "__main__":
    main()
    
    
    



'''
--Main Response Details--
pet_name
large_results_photo_url : may need to pad image based on resolution
primary_breed
secondary_breed
sex
age
pet_id
size
--Pet Details--
species : eg. dog, cat
color


pet_details_url : link on website
images : list of bottom image thumbnails 

    "images": [
      {
        "thumbnail_url": "https://media.adoptapet.com/image/upload/d_PDP-NoPetPhoto_Dog.png/c_auto,g_auto,w_135,ar_27:28,dpr_2/f_auto,q_auto/1260720709",
        "thumbnail_width": 135,
        "thumbnail_height": 140,
        "original_url": "https://media.adoptapet.com/image/upload/d_PDP-NoPetPhoto_Dog.png/c_auto,g_auto,w_358,ar_142:135,dpr_2/f_auto,q_auto/1260720709",
        "original_width": 358,
        "original_height": 341
      },
      {
        "thumbnail_url": "https://media.adoptapet.com/image/upload/d_PDP-NoPetPhoto_Dog.png/c_auto,g_auto,w_135,ar_27:28,dpr_2/f_auto,q_auto/1260720718",
        "thumbnail_width": 135,
        "thumbnail_height": 140,
        "original_url": "https://media.adoptapet.com/image/upload/d_PDP-NoPetPhoto_Dog.png/c_auto,g_auto,w_358,ar_142:135,dpr_2/f_auto,q_auto/1260720718",
        "original_width": 358,
        "original_height": 341
      },
      {
        "thumbnail_url": "https://media.adoptapet.com/image/upload/d_PDP-NoPetPhoto_Dog.png/c_auto,g_auto,w_135,ar_27:28,dpr_2/f_auto,q_auto/1260720724",
        "thumbnail_width": 135,
        "thumbnail_height": 140,
        "original_url": "https://media.adoptapet.com/image/upload/d_PDP-NoPetPhoto_Dog.png/c_auto,g_auto,w_358,ar_142:135,dpr_2/f_auto,q_auto/1260720724",
        "original_width": 358,
        "original_height": 341
      }
    ]
'''