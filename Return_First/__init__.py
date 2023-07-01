from googlesearch import search


def get_first_link(query):
    # Perform the search and retrieve the URLs
    search_results = search(query, num_results=1, lang='en')

    # Extract the first URL from the search results
    first_link = next(search_results, None)

    return first_link


def well():
    query = input("Enter your search query: ")
    first_link = get_first_link(query)
    if first_link:
        return(first_link)
    else:
        print("No link found.")
