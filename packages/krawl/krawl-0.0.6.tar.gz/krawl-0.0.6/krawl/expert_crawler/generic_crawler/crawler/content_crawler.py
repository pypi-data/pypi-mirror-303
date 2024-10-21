"""
Example
-------
>>> python companyshot/mine_landingpage.py check https://www.glean.ai/
"""

from typing import Callable, Optional

from krawl.common import singleton
from krawl.common.flow import CrawlerBase
from krawl.common.recognizers import MainTextRecognizer, SoupGrabber
from krawl.common.schema.dtypes import Href, HtmlFlagEnum, StructuredResponse
from krawl.common.soup_utils import HtmlPageReader
from krawl.common.textware import TextFilter


@singleton
class GenericCrawler(CrawlerBase):

    def __init__(self):
        self.reader = HtmlPageReader()
        self.text_getter = MainTextRecognizer()

        # TODO STORE HOSTS where bs4 failed to fastforward to selenium

    def check_content(
        self,
        url: str
    ) -> str:
        soup = self.reader.get_soup(url=url)
        text = self.text_getter.check(node=soup, base_url=url)
        return text

    def check_content_structured(
        self,
        url: str,
        see: set = {"*"},
        link_filter: Optional[Callable] = None
    ) -> StructuredResponse:

        try:
            soup = self.reader.get_soup(url=url)
            text = self.text_getter.check(soup, base_url=url)
            if len(text) < 200:
                soup_new = self.reader.get_soup_heavy(url=url,
                                                      reason="TooShort")
                text = self.text_getter.check(soup_new, base_url=url)
                if "security check" in text[0:400]:
                    print("[BYPASS] Capcha")
                    status = HtmlFlagEnum.B01
                else:
                    soup = soup_new
                    status = HtmlFlagEnum.B00
            else:
                status = HtmlFlagEnum.A00
        except Exception as err:
            print(f"SOUPERR: {err}")
            status = HtmlFlagEnum.E00
        if (
            status not in (HtmlFlagEnum.A00, HtmlFlagEnum.B00)
        ):
            # https://www.mri.tum.de/sites/default/files/seiten/jahresbericht_wald.pdf
            # mailto:office.ethics@mh.tum.de
            # http://www.dhm.mhn.de/de/kliniken_und_institute/klink_fuer_kinderkardiologie_u.cfm
            # SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1000)')))...
            return StructuredResponse(
                title="",
                h1=[],
                h2=[],
                text="",
                links=[],
                coretext="",
                image_url_primary="",
                origin=url,
                status=status
            )

        # Check what to see
        see_all = "*" in see
        see_title = "title" in see or see_all
        see_h1 = "h1" in see or see_all
        see_h2 = "h2" in see or see_all
        see_text = "text" in see or see_all
        see_links = "links" in see or see_all
        see_image = "image" in see or see_all

        text = self.text_getter.check(soup, base_url=url) if see_text else ""
        if see_links:
            links = SoupGrabber.links(
                soup=soup,
                base_url=url,
                filter_condition=link_filter
            )
            ilinks = SoupGrabber.inbound_links(soup=soup, base_url=url)
            olinks = SoupGrabber.outbound_links(soup=soup, base_url=url)
        else:
            links = ilinks = olinks = []
        img = SoupGrabber.image_primary(soup, url) if see_image else ""
        resp = StructuredResponse(
            title=SoupGrabber.title(soup=soup) if see_title else "",
            h1=SoupGrabber.h1_all(soup=soup) if see_h1 else [],
            h2=SoupGrabber.h2_all(soup=soup) if see_h2 else [],
            text=text,
            coretext=TextFilter.corepart(text),
            links=[Href(**item) for item in links],
            ilinks=[Href(**item) for item in ilinks],
            olinks=[Href(**item) for item in olinks],
            image_url_primary=img,
            origin=url,
            status=status
        )
        return resp
