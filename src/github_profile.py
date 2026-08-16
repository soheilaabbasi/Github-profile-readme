from pathlib import Path


def generate_profile(theme, **kwargs):

    # Read theme
    with open(f"src/themes/{theme}/profile.txt") as f:
        profile = f.read()

    # Replace placeholders with user input
    for item, value in kwargs.items():
        item_path = Path(f"src/themes/{theme}/{item}.txt")
        if not item_path.exists():
            continue

        with open(item_path) as f:
            profile_item = f.read()


        profile_item = profile_item.replace("{ value }", value)
        #print(item, value, profile_item)
        profile = profile.replace(f"{{ {item} }}", profile_item)

    return profile


if __name__ == '__main__':
    # Personal Info
    name = "Jhon Doe"
    email = "johndoe@gmail.com"
    phone = "+1 123 456 7890"
    homepage = "https://johndoe.com"
    location = "New York, USA"

    # Social Media
    github = "jhondoe"
    linkedin = "jhondoe"
    twitter = "jhondoe"
    facebook = "jhondoe"
    instagram = "jhondoe"
    youtube = "jhondoe"
    mediun = "jhondoe"

    # Select Theme
    theme = "default"

    # Generate Readme
    profile = generate_profile(theme, name=name, email=email, linkedin=linkedin)
    print(profile)

   


   
   

