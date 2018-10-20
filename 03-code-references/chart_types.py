from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# insert the correct path to your driver
driver = webdriver.Chrome(executable_path=r"/Users/vahanm/desktop/05_code/chromedriver")
driver.get('http://google.com/imghp')

chart_types = [
    'Area chart',
    'Bar chart, clustered bar, stacked bar',
    'Box & Whisker',
    'Bubble comparison',
    'Chord',
    'Circle packing',
    'Circular column',
    'Confidence interval',
    'Connected dot plot',
    'Dendrogram',
    'Flowchart',
    'Gantt chart',
    'Gauge',
    'Heatmap chart',
    'Histogram',
    'Hive plot',
    'Line chart',
    'Marimekko chart',
    'Matrix chart, Co-occurrence matrix',
    'Network, Force directed',
    'Nightingale, polar chart',
    'Node-Link Tree',
    'Parallel coordinates',
    'Pictogram',
    'Pie chart, Donut chart',
    'Pyramid (population)',
    'Radar chart',
    'Sankey',
    'Scatter plot, connected scatterplot',
    'Slope chart',
    'Sparklines',
    'Stacked area',
    'Stream chart',
    'Sunburst',
    'Treemap',
    'Venn diagram',
    'Violin plot',
    'Voronoi',
    'Word cloud'
]


for input in range(len(chart_types)):
    result = driver.find_element_by_name('q')
    result.send_keys(chart_types[input])
    result.send_keys(Keys.RETURN)  # if you're running from windows change to Kyes.ENTER
    time.sleep(2)
    driver.execute_script("window.open('https://www.google.com/imghp');")
    driver.switch_to.window(driver.window_handles[input + 1])
