def get_blogs():
    blog = open("data/blog_posts.csv")
    blog_lines = blog.readlines()
    for i in range(1, len(blog_lines)):
        line = blog_lines[i].split(",")
        line[2] = str(line[2])+"/"+str(line[3])+"/"+str(line[4])
        line.pop(3)
        line.pop(3)
        line = line[0]+","+line[1]+","+line[2]+","+line[3]+","+line[4]+","+line[5]
        blog_lines[i] = line.split(",")
    return blog_lines

blogs = get_blogs()
for i in range(0, len(blogs)):
    print(blogs[i])