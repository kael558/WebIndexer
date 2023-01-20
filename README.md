<a name="readme-top"></a>

[![MIT License][license-shield]][license-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
[I][rahel-linkedin-url] created this project for [LabLab.ai's AI21 Labs Hackathon](https://lablab.ai/event/ai21-labs-hackathon). 

The existing search bar in most websites performs keyword search. A slow and arduous process in which the user has to read through a myriad of information before finding the tidbit that they wanted in the first place. 

My goal was to create a question answering tool that can be easily integrated into any website. It allows you to find specific information, provides answers in a clear, understandable way and includes sources and more information should the user need it.

Presenting Web Indexer. Developed to significantly improve the user experience by providing a service that ChatGPT, Google and standard search bars cannot. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [AI21 Labs]((https://www.ai21.com/)
* [Streamlit](https://streamlit.io/)
* [Cohere](https://cohere.ai/)
* [Scrapy](https://scrapy.org/)
* [Annoy](https://github.com/spotify/annoy)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### To Scrape a website:
1. Navigate to the spiders directory in the scraper directory
2. Change the urls and domains in the Spider class
3. Run the command in the terminal `scrapy crawl text -O ../data/{filename}.csv`
4. Specify pages to scrape with `CLOSESPIDER_PAGECOUNT = 10` in settings.py

### To see content of html file
1. Navigate to main directory
2. Run `scrapy shell <url>`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
* Choose the website you wish to scrape on the Streamlit server
* Enter a question that you would like answered
* Adjust the threshold and number of paragraphs to control the context

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
- [ ] Create benchmarks
- [ ] Summarize context? May lead to improved accuracy
- [ ] Conversation style with prior questions as context
- [ ] Finetune both embedding and generation models
- [ ] Access to attention layer for improved relevant links

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing
This repository is intended as an archive. No changes will be made to it in the future. 

You may fork the project and work in your own repository.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact
Rahel Gunaratne:
 - Email: rahel.gunaratne@gmail.com
 - [Twitter](https://twitter.com/gunaratne_rahel)
 - [LinkedIn](https://www.linkedin.com/in/rahelgunaratne/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues

[license-shield]: https://img.shields.io/github/license/kael558/WebIndexer.svg?style=for-the-badge
[license-url]: https://github.com/kael558/WebIndexer/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[rahel-linkedin-url]: https://www.linkedin.com/in/rahelgunaratne/
