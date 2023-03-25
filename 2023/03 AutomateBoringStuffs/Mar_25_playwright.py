""" 
Created on : 25/03/23 6:25 am
@author : ds  
"""

from playwright.sync_api import expect, sync_playwright


def test_dhanasekars(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = browser.new_page()
    page.goto('https://www.dhanasekars.com/')

    # Expect title to have Focused Life
    expect(page).to_have_title('Focused Life')

    # Expect a subscribe option on the home page
    subscribe = page.get_by_role("button")
    expect(subscribe).to_have_text("Subscribe")

    # Expect about link on the home page
    about = page.get_by_role("link", name="About")
    expect(about).to_have_text("About")
    expect(about).to_have_attribute("href", "/about")
    about.click()
    expect(page).to_have_title("About — Focused Life")
    context.tracing.stop(path="trace.zip")
    browser.close()


with sync_playwright() as playwright:
    test_dhanasekars(playwright)
