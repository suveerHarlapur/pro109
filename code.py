import statistics,pandas as pd,plotly.figure_factory as ff,plotly.graph_objects as go;
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_start, first_end = mean-std_deviation, mean+std_deviation
second_start, second_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_start, third_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_1_std_deviation = [result for result in data if result > first_start and result < first_end]
list_2_std_deviation = [result for result in data if result > second_start and result < second_end]
list_3_std_deviation = [result for result in data if result > third_start and result < third_end]
print("mean {}".format(mean))
print("median {}".format(median))
print("mode {}".format(mode))
print("standard deviation {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_3_std_deviation)*100.0/len(data)))

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[first_start, first_start], y=[0, 0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_end, first_end], y=[0, 0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_start, second_start], y=[0, 0.17], mode="lines", name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_end, second_end], y=[0, 0.17], mode="lines", name="standard deviation 2"))
fig.show()