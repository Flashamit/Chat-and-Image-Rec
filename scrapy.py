from langchain_community.document_loaders import WebBaseLoader


all_urls = ["https://www.lukecoutinho.com/",
            "https://www.lukecoutinho.com/about",
            "https://www.lukecoutinho.com/programs/wellness-program",
            "https://www.lukecoutinho.com/programs/exclusive-wellness-with-luke",
            "https://www.lukecoutinho.com/programs/executive-wellness-program-with-luke",
            "https://www.lukecoutinho.com/programs/cancer-care",
            "https://www.lukecoutinho.com/programs/cardiovascular-rehab-program",
            "https://www.lukecoutinho.com/programs/fertility-program",
            "https://www.lukecoutinho.com/programs/gut-health-program",
            "https://www.lukecoutinho.com/programs/hormonal-health",
            "https://www.lukecoutinho.com/programs/kidney-care-program",
            "https://www.lukecoutinho.com/programs/diabetes-care-program-",
            "https://www.lukecoutinho.com/programs/pregnancy-care-program",
            "https://www.lukecoutinho.com/programs/skin-care-program",
            "https://www.lukecoutinho.com/programs/sports-nutrition",
            "https://www.lukecoutinho.com/programs/thyroid-care-program"
            "https://www.lukecoutinho.com/weight_loss_program",
            "https://www.lukecoutinho.com/programs/emotional-wellness-homeopathy-program",
            "https://www.lukecoutinho.com/programs/balanced-nutrition-for-children",
            "https://www.lukecoutinho.com/programs/preventive-care-programs",
            "https://www.lukecoutinho.com/programs/rejuvenation-and-cleanse-program-",
            "https://www.lukecoutinho.com/programs/sattvik-program",
            "https://www.lukecoutinho.com/programs/post-cancer-care-program",
            "https://www.lukecoutinho.com/programs/basic-cancer-care-program",
            "https://lukecoutinho.com/blog/courses/",
            "https://lukecoutinho.com/blog/courses/page/2/",
            "https://lukecoutinho.com/blog/courses/page/3/",
            "https://lukecoutinho.com/blog/category/lifestyle-en/exercise-en/",
            "https://lukecoutinho.com/blog/lifestyle-en/exercise-en/burn-belly-fat/",
            "https://lukecoutinho.com/blog/lifestyle-en/various-health-benefits-of-vitamin-w-walking/",
            "https://lukecoutinho.com/blog/lifestyle-en/why-heart-disease-is-the-leading-cause-of-mortality/",
            "https://lukecoutinho.com/blog/lifestyle-en/exercise-en/exercises-to-burn-fat-and-keep-muscles-lean-and-firm-while-travelling/",
            "https://lukecoutinho.com/blog/condition-management-en/weight-management-en/rest-based-training-fat-loss-lean-mass-immunity-and-metabolism/",
            "https://lukecoutinho.com/blog/lifestyle-en/exercise-en/why-your-joints-ache/",
            "https://lukecoutinho.com/blog/condition-management-en/weight-management-en/unable-to-loose-belly-fat-even-with-regular-exercise/",
            "https://lukecoutinho.com/blog/category/lifestyle-en/sleep-en/",
            "https://lukecoutinho.com/blog/lifestyle-en/vagus-nerve-technique/",
            "https://lukecoutinho.com/blog/2024/sleep-reset-exercise/",
            "https://lukecoutinho.com/blog/lifestyle-en/training-on-sleep-deprived-body/",
            "https://lukecoutinho.com/blog/lifestyle-en/sleep-en/how-can-late-night-workers-have-an-improved-sleeping-schedule/",
            "https://lukecoutinho.com/blog/lifestyle-en/sleep-en/follow-these-pre-bedtime-rituals-for-a-deep-and-sound-sleep/",
            "https://lukecoutinho.com/blog/lifestyle-en/sleep-en/top-3-breathing-techniques-to-sleep-like-a-baby/",
            "https://lukecoutinho.com/blog/holistic-health-store/why-smartgrid-mattress-is-the-answer/",
            "https://lukecoutinho.com/blog/lifestyle-en/sleep-en/here-is-why-many-people-find-it-difficult-to-wake-up-in-the-morning/",
            "https://lukecoutinho.com/blog/lifestyle-en/top-15-holistic-tips-to-handle-insomnia-sleep-issues/",
            "https://lukecoutinho.com/blog/lifestyle-en/sleep-en/dont-compromise-on-your-sleep/",
            "https://lukecoutinho.com/blog/lifestyle-en/breathing-techniques-to-sleep-better/",
            "https://lukecoutinho.com/blog/category/lifestyle-en/healthy-diy/",
            "https://lukecoutinho.com/blog/category/lifestyle-en/seniors-health/",
            "https://lukecoutinho.com/blog/category/lifestyle-en/child-health-en/",
            "https://lukecoutinho.com/blog/category/condition-management-en/cancer-en/",
            "https://lukecoutinho.com/blog/category/condition-management-en/mental-health-en/",
            "https://lukecoutinho.com/blog/category/condition-management-en/weight-management-en/",
            "https://lukecoutinho.com/blog/category/condition-management-en/pregnancy/",
            "https://lukecoutinho.com/blog/category/lifestyle-en/womens-health-en/",
            "https://lukecoutinho.com/blog/category/beyond-medicine/immunity/",
            "https://lukecoutinho.com/blog/category/beyond-medicine/yoga-and-meditation/",
            "https://lukecoutinho.com/blog/category/nutrition-en/intermittent-fasting/",
            "https://lukecoutinho.com/blog/category/recipe-corner/",
            "https://lukecoutinho.com/blog/category/youcare-products-science/",
            "https://lukecoutinho.com/blog/category/success-stories/"]


for data in all_urls:
    loader = WebBaseLoader(data)
    docs = loader.load()

input_file = "Luke_data.txt"
with open(input_file, "w", encoding="utf-8") as file:
    for doc in docs:
        file.write(f"Title: {doc.metadata.get('title', 'No Title')}\n")
        file.write(f"Content:\n{doc.page_content}\n")
        file.write("=" * 80 + "\n")



# Data Cleaning 

output_file = "Luke_data_cleaned.txt"

with open(input_file, "r", encoding="utf-8") as infile:
    with open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            
            cleaned_line = ' '.join(line.split())
           
            outfile.write(cleaned_line + "\n")

