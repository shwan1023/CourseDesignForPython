
$(function () {
    map();
    function map() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('map_1'));
var data = [
     {name: '青岛房价', value: 14058.00},
     {name: '上海房价', value: 36741.00},
     {name: '厦门房价', value: 33779},
     {name: '昆明房价', value: 12212},
     {name: '沈阳房价', value: 11617},
     {name: '成都房价', value: 12148},
     {name: '重庆房价', value: 8917},
     {name: '南京房价', value: 24682},
     {name: '北京房价', value:42684.00},
     {name: '杭州房价', value: 27448},
     {name: '济南房价', value: 12282},
     {name: '天津房价', value: 16391},
     {name: '武汉房价', value: 14244},
     {name: '深圳房价', value: 56844},
     {name: '石家庄房价', value: 9869},
     {name: '合肥房价', value:14321.00},
     {name: '福州房价', value: 13520},
     {name: '西安房价', value: 13358},
     {name: '南昌房价', value: 10978},
     {name: '哈尔滨房价', value: 9467},
     {name: '长春房价', value: 9081}
];
var geoCoordMap = {
    '青岛房价':[120.33,36.07],
    '上海房价':[121.48,31.22],
    '厦门房价':[118.1,24.46],
    '广州房价':[113.23,23.16],
    '昆明房价':[102.73,25.04],
    '深圳房价':[114.07,22.62],
    '沈阳房价':[123.38,41.8],
    '成都房价':[104.06,30.67],
    '重庆房价':[106.54,29.59],
    '南京房价':[118.78,32.04],
    '北京房价':[116.46,39.92],
    '杭州房价':[120.19,30.26],
    '济南房价':[117,36.65],
    '天津房价':[117.2,39.13],
    '武汉房价':[114.31,30.52],
    '石家庄房价':[114.48,38.03],
    '合肥房价':[117.27,31.86],
    '福州房价':[119.3,26.08],
    '西安房价':[108.95,34.27],
    '哈尔滨房价':[126.63,45.75],
    '长春房价':[125.35,43.88],
    '南昌房价':[115.89,28.68]

};
var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

option = {
   // backgroundColor: '#404a59',
  /***  title: {
        text: '实时行驶车辆',
        subtext: 'data from PM25.in',
        sublink: 'http://www.pm25.in',
        left: 'center',
        textStyle: {
            color: '#fff'
        }
    },**/
    tooltip : {
        trigger: 'item',
		formatter: function (params) {
              if(typeof(params.value)[2] == "undefined"){
              	return params.name + ' : ' + params.value;
              }else{
              	return params.name + ' : ' + params.value[2];
              }
            }
    },
  
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        roam: false,//禁止其放大缩小
        itemStyle: {
            normal: {
                areaColor: '#4c60ff',
                borderColor: '#002097'
            },
            emphasis: {
                areaColor: '#293fff'
            }
        }
    },
    series : [
        {
            name: '消费金额',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(data),
            symbolSize: function (val) {
                return val[2] / 1300;
            },
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: false
                },
                emphasis: {
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#ffeb7b'
                }
            }
        }
		
		/**
		,
        {
            name: 'Top 5',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            data: convertData(data.sort(function (a, b) {
                return b.value - a.value;
            }).slice(0, 6)),
            symbolSize: function (val) {
                return val[2] / 20;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#ffd800',
                    shadowBlur: 10,
                    shadowColor: 'rgba(0,0,0,.3)'
                }
            },
            zlevel: 1
        }
		**/
    ]
};
		
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

})

