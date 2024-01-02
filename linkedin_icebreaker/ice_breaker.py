from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties import linkedin
from agents import linkedin_lookup_agent

information = """
Anil Kapoor (born 24 December 1956) is an Indian actor and producer who works primarily in Hindi films, besides television and international films.[1] In a career spanning over 40 years as an actor and since 2005 as a producer, Kapoor has appeared in more than 100 films. Recognised for multiple iconic, popular and cult films, he has received several accolades including two National Film Awards and seven Filmfare Awards.

Born to film producer Surinder Kapoor, he made his Bollywood debut with a small role in the romance Hamare Tumhare (1979) before starring in the Telugu film Vamsa Vruksham (1980) and Kannada film Pallavi Anupallavi (1983). His career saw a turning point with the action drama Mashaal (1984), before he established himself as a leading man with his roles in Meri Jung (1985), Karma (1986), Mr. India (1987), Tezaab (1988), Ram Lakhan (1989) and Eeshwar (1989). Kapoor's other commercially successful films include Lamhe (1991), Benaam Badsha (1991), Beta (1992), 1942: A Love Story (1994), Andaz (1994), Laadla (1994), Trimurti (1995), Loafer (1996), Virasat (1997), Judaai (1997), Deewana Mastana (1997), Gharwali Baharwali (1998), Taal (1999), Hum Aapke Dil Mein Rehte Hain (1999), Biwi No. 1 (1999), Pukar (2000), Lajja (2001), Nayak (2001), No Entry (2005), Welcome (2007), Black & White (2008), Race (2008), Race 2 (2013), Shootout at Wadala (2013), Dil Dhadakne Do (2015), Welcome Back (2015), Race 3 (2018), Total Dhamaal (2019), Malang (2020), AK vs AK (2020), Thar (2022), Jugjugg Jeeyo (2022), and Animal (2023).

Kapoor's first role in an international film was in Danny Boyle's Academy Award-winning film Slumdog Millionaire, for which he shared the Screen Actors Guild Award for Outstanding Performance by a Cast in a Motion Picture.[3] His performance in the eighth season of the action series 24 generated rave reviews from the American press.[4][5] Globally, Kapoor is one of the most recognised Indian film actors.[6]s
"""

if __name__ == "__main__":
    print("Hello Langchain!!")
    name = "Eden Marco"
    linkedin_profile_url = linkedin_lookup_agent.lookup(name=name)
    print(f"User: {name}; LinkedIn URL: {linkedin_profile_url}")

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary.
        2. two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0.0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = linkedin.scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url, dummy=False
    )
    print(f"Prompt : {summary_template}")
    print(f"linkedin_data: {linkedin_data}")
    print(chain.run(information=linkedin_data))

