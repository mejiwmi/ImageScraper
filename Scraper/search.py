import time
from ddgs import DDGS

def search_image(query, max_results):
    results=[]
    with DDGS() as ddg_s:
        for result in ddg_s.images(query=query, max_results=max_results, safesearch='off'):
            if 'image' in result and result['image'].startswith('http'):
                results.append(result['image'])
            if len(results) >= max_results:
                break
            time.sleep(0.5) # increment it if temporary blockage is experienced
    return results