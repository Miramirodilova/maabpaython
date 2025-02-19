
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\n"


class Blog:
    def __init__(self):
        self.posts = []  

    def add_post(self, post):
        self.posts.append(post) 

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for post in self.posts:
            print(post)

    def display_post_by_author(self, author):
        filtered_posts = [post for post in self.posts if post.author == author]
        if not filtered_posts:
            print("No posts found for this author.")
        for post in filtered_posts:
            print(post)

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]
        print(f"Post '{title}' deleted.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print(f"Post '{title}' updated.")
                return
        print("Post not found.")

    def display_latest_post(self):
        if self.posts:
            print(self.posts[-1])
        else:
            print("No posts available.")


def main():
    blog = Blog()
    while True:
        print("\nBlog System Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Edit a Post")
        print("5. Delete a Post")
        print("6. Display Latest Post")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            content = input("Enter content: ").strip()
            author = input("Enter author: ").strip()
            blog.add_post(Post(title, content, author)) 

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter author's name: ").strip()
            blog.display_post_by_author(author)  

        elif choice == "4":
            title = input("Enter post title to edit: ").strip()
            new_content = input("Enter new content: ").strip()
            blog.edit_post(title, new_content)

        elif choice == "5":
            title = input("Enter post title to delete: ").strip()
            blog.delete_post(title)

        elif choice == "6":
            blog.display_latest_post()

        elif choice == "7":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()


students = [
    ("Alice", [85, 90, 78]),
    ("Bob", [70, 65, 80]),
    ("Charlie", [95, 100, 98]),
    ("David", [55, 60, 50]),
    ("Eva", [88, 92, 85])
]

threshold = 80

qualified_scores = []
for name, scores in students:
    if any(score > threshold for score in scores):  
        qualified_scores.extend(scores)  

average_score = sum(qualified_scores) / len(qualified_scores) if qualified_scores else 0

print(average_score)

a=[1,2,3,4,5,6,7,8,9,10]
b=a
b.append(11)
print(a)
