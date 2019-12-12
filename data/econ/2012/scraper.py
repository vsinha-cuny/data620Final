
import arxiv
import arxivchecker

# https://pypi.org/project/arxiv-checker/

p1 = arxivchecker.scrape_arxiv('econ',year=2012,month='all')

for x in list(p1):
    print(x)
    url1 = "http://arxiv.org/pdf/" + x
    title1 = x
    paper1 = {"pdf_url": url1, "title": title1}
    arxiv.download(paper1)

