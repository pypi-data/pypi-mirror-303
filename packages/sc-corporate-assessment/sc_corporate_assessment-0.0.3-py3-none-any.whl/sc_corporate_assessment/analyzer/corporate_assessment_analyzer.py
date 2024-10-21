#  The MIT License (MIT)
#
#  Copyright (c) 2024. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import logging
import os
import os.path
from datetime import datetime, timedelta

import pandas as pd
from config42 import ConfigManager

from sc_corporate_assessment import PROJECT_NAME, __version__
from .base_analyzer import BaseAnalyzer


class CorporateAssessmentAnalyzer(BaseAnalyzer):
    """
    对公结算户考核分析
    """

    def __init__(self, *, config: ConfigManager, excel_writer: pd.ExcelWriter):
        super().__init__(config=config, excel_writer=excel_writer)
        self._key_enabled = "corporate.sales_summary.enabled"
        self._key_business_type = "corporate.sales_summary.business_type"

    def _read_config(self, *, config: ConfigManager):
        # 报表文件路径
        self._src_filepath = config.get("corporate.sales_summary.source_file_path")
        # 日期格式
        self._date_format = config.get("corporate.sales_summary.date_format")
        # 分析开始日期
        self._start_date_str = config.get("corporate.sales_summary.start_date")
        self._start_date = datetime.strptime(self._start_date_str, self._date_format)
        # 分析结束日期
        self._end_date_str = config.get("corporate.sales_summary.end_date")
        self._end_date = datetime.strptime(self._end_date_str, self._date_format)

        # Sheet名称
        self._sheet_name = config.get("corporate.sales_summary.sheet_name")
        self._total_bonus_column_name = config.get("corporate.sales_summary.total_bonus_column_name")
        # 列名添加后缀
        self._column_suffix = config.get("corporate.sales_summary.column_suffix")
        # 表头行索引
        self._header_row = config.get("corporate.sales_summary.header_row")
        self._account_name_column = self._calculate_column_index_from_config(
            config, "corporate.sales_summary.account_name_column"
        )
        self._account_no_column = self._calculate_column_index_from_config(
            config, "corporate.sales_summary.account_no_column"
        )
        self._deposit_period_column = self._calculate_column_index_from_config(
            config, "corporate.sales_summary.deposit_period_column"
        )
        self._filtered_deposit_period_name = config.get("corporate.sales_summary.filtered_deposit_period_name")
        self._pos_column = self._calculate_column_index_from_config(
            config, "corporate.sales_summary.pos_column"
        )
        bonus_unit_str = config.get("corporate.sales_summary.bonus_unit")
        self._bonus_unit = 100
        try:
            self._bonus_unit = int(bonus_unit_str)
        except ValueError:
            # ignore
            logging.getLogger(__name__).error("配置项 {} 配置错误".format("corporate.sales_summary.bonus_unit"))
        bonus_amount_per_unit = config.get("corporate.sales_summary.bonus_amount_per_unit")
        self._bonus_amount_per_unit = 3
        try:
            self._bonus_amount_per_unit = int(bonus_amount_per_unit)
        except ValueError:
            # ignore
            logging.getLogger(__name__).error(
                "配置项 {} 配置错误".format("corporate.sales_summary.bonus_amount_per_unit"))

    def _calculate_daily_summary(self, date: datetime):
        date_str = date.strftime(self._date_format)
        filename = self._src_filepath.format(date_str)
        logging.getLogger(__name__).info("读取源文件：{}".format(filename))
        if not os.path.exists(filename):
            logging.getLogger(__name__).error("无法找到源文件：{}".format(filename))
            return pd.DataFrame()
        data = pd.read_csv(filename, header=self._header_row)
        self._account_name_column_name = data.columns[self._account_name_column]
        self._account_no_column_name = data.columns[self._account_no_column]
        self._deposit_period_column_name = data.columns[self._deposit_period_column]
        self._pos_column_name = data.columns[self._pos_column]
        # 仅选择活期存款
        criterion = data[self._deposit_period_column_name].map(lambda x: x == self._filtered_deposit_period_name)
        data = data[criterion].copy()
        # 按账户名称、单位账号统计
        self._index_columns = [self._account_name_column_name, self._account_no_column_name]
        # 统计单位时点数列
        self._value_columns = [self._pos_column_name]
        # 统计时点数
        table = pd.pivot_table(
            data,
            values=self._value_columns,
            index=self._index_columns,
            aggfunc="sum",
            fill_value=0,
        )
        data = table.reset_index()
        # 统计列重命名为统计日期
        data.rename(columns={self._pos_column_name: date_str}, inplace=True)
        # 填充数据
        data.fillna(0, inplace=True)
        return data

    # 定义奖励计算函数
    def _calculate_rewards_for_row(self, row):
        rewards = [0]  # 第一天不计算奖励
        previous_amount = 0  # 前一天的存款量
        previous_retained_amount = 0  # 前日保有

        for i in range(len(row)):
            new_deposit = 0  # 当日新增
            decreased_amount = 0  # 当日减少
            current_amount = row.iloc[i]

            if i == 0:
                previous_amount = current_amount
                continue  # 第一行不计算奖励

            # 计算新增、减少金额
            inc_amount = current_amount - previous_amount
            if inc_amount > 0:
                new_deposit = inc_amount
            else:
                decreased_amount = -inc_amount

            # 计算当日保有金额
            retained_amount = previous_retained_amount - decreased_amount

            # 保有金额不能为负
            if retained_amount < 0:
                retained_amount = 0

            # 计算奖励
            new_deposit_reward = self._calculate_bonus(new_deposit)
            retained_reward = self._calculate_bonus(retained_amount)

            # 总奖励 = 新增奖励 + 保有奖励
            total_reward = new_deposit_reward + retained_reward
            rewards.append(total_reward)

            # 更新前一天的存款量
            previous_amount = current_amount
            # 计算明天的“前日保有”
            previous_retained_amount = retained_amount + new_deposit

        return rewards

    def _calculate_rewards(self, df: pd.DataFrame) -> pd.DataFrame:
        # 对每一行（每个公司）应用计算函数
        rewards_df = df.apply(self._calculate_rewards_for_row, axis=1)

        # 将结果转换为 DataFrame 并设置日期列
        rewards_df = pd.DataFrame(rewards_df.tolist(), columns=df.columns, index=df.index)
        rewards_df = rewards_df.add_suffix(self._column_suffix)
        # 计算总奖励金额
        rewards_df[self._total_bonus_column_name] = rewards_df.iloc[:, 1:].sum(axis=1)
        return rewards_df

    def _calculate_bonus(self, amount):
        return (amount // self._bonus_unit) * self._bonus_amount_per_unit

    def analysis_new(self) -> int:
        """
        主分析流程分析
        """
        logging.getLogger(__name__).info("program {} version {}".format(PROJECT_NAME, __version__))
        self._business_type = self._config.get(self._key_business_type)
        # 如果未启用，则直接返回上一次的分析数据
        if not self._enabled():
            # 处理缺少配置的情况下日志记录不到具体分析类型的问题
            business_type = self._business_type
            if business_type is None:
                business_type = self._key_business_type
            logging.getLogger(__name__).info("{} 分析未启用".format(business_type))
            return 1
        # 读取业务类型
        logging.getLogger(__name__).info("开始分析 {} 数据".format(self._business_type))

        logging.getLogger(__name__).info("读取源文件：{}".format(self._src_filepath))
        # 基准日的数据
        base_data = self._calculate_daily_summary(self._start_date)
        result = base_data.copy()

        # 所有列名（用来最后排序列名）
        columns = self._index_columns.copy()
        columns.append(self._start_date_str)

        cur_date = self._start_date
        cur_date += timedelta(days=1)
        while cur_date <= self._end_date:
            cur_date_str = cur_date.strftime(self._date_format)
            logging.getLogger(__name__).info("开始分析日期 {} 的数据...".format(cur_date_str))
            # 计算统计日期的数据
            data = self._calculate_daily_summary(cur_date)
            if data.empty:
                logging.getLogger(__name__).error("日期 {} 无数据".format(cur_date_str))
                cur_date += timedelta(days=1)
                continue
            # 与基准日数据合并
            result = result.merge(
                data,
                how="outer",
                left_on=self._index_columns,
                right_on=self._index_columns,
            )
            columns.append(cur_date_str)
            # 给对应日期添加奖励列
            columns.append(cur_date_str + self._column_suffix)

            cur_date += timedelta(days=1)
            logging.getLogger(__name__).info("结束分析日期 {} 的数据".format(cur_date_str))

        # 填充数据
        result.fillna(0, inplace=True)

        # 计算每日奖励
        temp_df = result.set_index(self._index_columns)
        rewards = self._calculate_rewards(temp_df)
        rewards.reset_index(inplace=True)
        # 总奖励金额列
        columns.append(self._total_bonus_column_name)

        # 与原始数据合并
        merged = result.merge(
            rewards,
            how="outer",
            left_on=self._index_columns,
            right_on=self._index_columns,
        )
        # 调整列名顺序
        merged = merged[columns]
        logging.getLogger(__name__).info("输出分析结果数据...")
        merged.to_excel(
            excel_writer=self._excel_writer,
            index=False,
            sheet_name=self._business_type,
        )
        logging.getLogger(__name__).info("完成分析 {} 数据".format(self._business_type))
        return 0
