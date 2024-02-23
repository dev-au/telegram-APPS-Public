import asyncio
import json

import aiohttp
from bs4 import BeautifulSoup

from typing import List, Union


class IslomUz:
    class SearchResults:
        question_paragraph: str
        answer_url: str

    class QuestionResults:
        question: str
        answer: str

    async def __fetch_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    def __convert_html(self, content_text) -> BeautifulSoup:
        soup = BeautifulSoup(content_text, 'html.parser')
        return soup

    def __convert_json(self, content_text) -> list:
        return json.loads(content_text)

    async def search_topic(self, sub_text) -> List[SearchResults]:
        url = f"https://savollar.islom.uz/searchauto?term={sub_text}"
        content_text = await self.__fetch_page(url)
        json_data = self.__convert_json(content_text)
        list_results = []
        for info in json_data:
            search_result = self.SearchResults()
            search_result.question_paragraph = info['value']
            search_result.answer_url = info['url']
            list_results.append(search_result)
        return list_results

    async def get_info(self, search_result: str) -> QuestionResults:
        url = f"https://savollar.islom.uz{search_result}"
        content_text = await self.__fetch_page(url)
        html_data = self.__convert_html(content_text)
        question_result = self.QuestionResults()
        question_result.question = html_data.find('div', class_='text_in_question').get_text().strip()
        question_result.answer = html_data.find('div', class_='answer_in_question').get_text().strip()
        return question_result
