(function () {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".box8 .echarts"), "dark");

  // 2. 指定配置和数据
  //数据纯属虚构
var data = [
  { name: "上海", value: 110000.0 },
  { name: "云南", value: 80000.0 },
  { name: "内蒙古", value: 50000.0 },
  { name: "北京", value: 114000.0 },
  { name: "吉林", value: 57500.0 },
  { name: "四川", value: 60000.0 },
  { name: "天津", value: 80000.0 },
  { name: "宁夏", value: 51500.0 },
  { name: "安徽", value: 71000.0 },
  { name: "山东", value: 70000.0 },
  { name: "山西", value: 50000.0 },
  { name: "广东", value: 90000.0 },
  { name: "广西", value: 65000.0 },
  { name: "新疆", value: 46000.0 },
  { name: "江苏", value: 96000.0 },
  { name: "江西", value: 68000.0 },
  { name: "河北", value: 57000.0 },
  { name: "河南", value: 50000.0 },
  { name: "浙江", value: 95000.0 },
  { name: "海南", value: 100000.0 },
  { name: "湖北", value: 105000.0 },
  { name: "湖南", value: 70000.0 },
  { name: "甘肃", value: 52600.0 },
  { name: "福建", value: 55000.0 },
  { name: "贵州", value: 70000.0 },
  { name: "辽宁", value: 60000.0 },
  { name: "重庆", value: 40000.0 },
  { name: "陕西", value: 60000.0 },
  { name: "青海", value: 89000.0 },
  { name: "黑龙江", value: 50000.0 },
];
data.sort((a, b) => b.value - a.value);

  var yData = [];
  var barData = [];

  for (var i = 0; i < 10; i++) {
    barData.push(data[i]);
    yData.push(i + data[i].name);
  }

  var option = {
    backgroundColor: "transparent", // Set background color to transparent
    title: [
      {
        show: true,
        text: "排名情况",
        textStyle: {
          color: "#2D3E53",
          fontSize: 18,
        },
        right: 20000,
        top: 1500000,
      },
    ],
    tooltip: {
      show: true,
      formatter: function (params) {
        return params.name + "：" + params.data["value"];
      },
    },
    visualMap: {
      type: "continuous",
      orient: "horizontal",
      itemWidth: 10,
      itemHeight: 80,
      text: ["高", "低"],
      showLabel: true,
      seriesIndex: [0],
      min: 40000,
      max: 120000,
      inRange: {
        color: ["#9eb7e5", "#648de5", "#304c89", "#05299e"],
      },
      textStyle: {
        color: "#7B93A7",
      },
      bottom: 30,
      left: "left",
    },
    grid: {
      right: 10,
      top: 135,
      bottom: 100,
      width: "20%",
    },
    xAxis: {
      show: false,
    },
    yAxis: {
      type: "category",
      inverse: true,
      nameGap: 16,
      axisLine: {
        show: false,
        lineStyle: {
          color: "#ddd",
        },
      },
      axisTick: {
        show: false,
        lineStyle: {
          color: "#ddd",
        },
      },
      axisLabel: {
        interval: 0,
        margin: 85,
        textStyle: {
          color: "#455A74",
          align: "left",
          fontSize: 14,
        },
        rich: {
          a: {
            color: "#fff",
            backgroundColor: "#05299e",
            width: 20,
            height: 20,
            align: "center",
            borderRadius: 2,
          },
          b: {
            color: "#fff",
            backgroundColor: "#4197FD",
            width: 20,
            height: 20,
            align: "center",
            borderRadius: 2,
          },
        },
        formatter: function (params) {
          if (parseInt(params.slice(0, 1)) < 3) {
            return [
              "{a|" +
                (parseInt(params.slice(0, 1)) + 1) +
                "}" +
                "  " +
                params.slice(1),
            ].join("\n");
          } else {
            return [
              "{b|" +
                (parseInt(params.slice(0, 1)) + 1) +
                "}" +
                "  " +
                params.slice(1),
            ].join("\n");
          }
        },
      },
      data: yData,
    },
    geo: {
      // roam: true,
      map: "china",
      left: "15",
      right: "300",
      // layoutSize: '80%',
      label: {
        emphasis: {
          show: false,
        },
      },
      itemStyle: {
        emphasis: {
          areaColor: "#7cabb1",
        },
      },
    },
    series: [
      {
        name: "mapSer",
        type: "map",
        roam: false,
        geoIndex: 0,
        label: {
          show: false,
        },
        data: data,
      },
      {
        name: "barSer",
        type: "bar",
        roam: false,
        visualMap: false,
        zlevel: 2,
        barMaxWidth: 8,
        barGap: 0,
        itemStyle: {
          normal: {
            color: function (params) {
              // build a color map as your need.
              var colorList = [
                {
                  colorStops: [
                    {
                      offset: 0,
                      color: "#eee", // 0% 处的颜色
                    },
                    {
                      offset: 1,
                      color: "#05299e", // 100% 处的颜色
                    },
                  ],
                },
                {
                  colorStops: [
                    {
                      offset: 0,
                      color: "#00C0FA", // 0% 处的颜色
                    },
                    {
                      offset: 1,
                      color: "#2F95FA", // 100% 处的颜色
                    },
                  ],
                },
              ];
              if (params.dataIndex < 3) {
                return colorList[0];
              } else {
                return colorList[1];
              }
            },
            barBorderRadius: 15,
          },
        },
        data: barData,
      },
    ],
  };
  myChart.setOption(option);

  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
