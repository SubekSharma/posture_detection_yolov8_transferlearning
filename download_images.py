from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
keywords = ["male buzz cut","male undercut","male crewcut", 
	    "hale temple fade", "male pompadour", "male comb over",
		"male man bun","male long hair"]
for kw in keywords: 
	response().download(kw,50)