## 数据

tick数据增加现手字段(tickvol)，即当前tick累计成交量与上条数据的差值

## 功能

xtdata.get_option_detail_data()期权多空方向类型判断调整

xtdata.get_trading_calendar() 自动下载所需的节假日数据

xtdata.get_instrument_detail() 字段ExpireDate类型由int调整为str

新增函数xtdata.get_formula_result()，用于获取subscribe_formula()的模型结果

## 修复

修复token模式下启用K线全推后单支订阅数据周期错误的问题