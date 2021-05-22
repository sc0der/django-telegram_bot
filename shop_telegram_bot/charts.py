from vali.charts import ModelCharts
from big_shop.models import Product


class ChartCounter(ModelCharts):
    model = Product
    chart_type = 'Bar'
    name = '123'
    labels = ["2018-03-01", "2018-03-02", "2018-03-03", "2018-03-04", "2018-03-05"]
    datasets = [
        {
            "label": "dataset 1",
            "fillColor": "rgba(220,220,220,0.2)",
            "strokeColor": "rgba(220,220,220,1)",
            "pointColor": "rgba(220,220,220,1)",
            "pointStrokeColor": "#fff",
            "pointHighlightFill": "#fff",
            "pointHighlightStroke": "rgba(220,220,220,1)",
            "data": [65, 59, 80, 81, 80]
        },
        {
            "label": "dataset 2",
            "fillColor": "rgba(151,187,205,0.2)",
            "strokeColor": "rgba(151,187,205,1)",
            "pointColor": "rgba(151,187,205,1)",
            "pointStrokeColor": "#fff",
            "pointHighlightFill": "#fff",
            "pointHighlightStroke": "rgba(151,187,205,1)",
            "data": [28, 48, 40, 19, 69]
        }
    ] 