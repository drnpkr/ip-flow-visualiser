# This program was forked from the work by Bo Hua Ruan (mona@ruan.co.nz) as part of her ENGR489 project
# The program reads in CSV files and interpret them in an Angular Historgram-like form
# The flow featuers used in this project were generated via flowRecorder
# For instructions on how to use flowRecorder see https://github.com/drnpkr/flowRecorder

import csv
import numpy as np
import matplotlib.pyplot as plt
import pygal
import pandas as pd
import timeit

plt.rc('text', usetex = False)
plt.rc('font', family ='serif')
plt.rcParams['figure.figsize'] = 10, 10


numID = []
flowID = []
bwdPktID = []
srcIP = []
srcPort = []
dstIP = []
dstPort = []
proto = []
bi_pktTotalCount = []
bi_octetTotalCount = []
bi_min_ps = []
bi_max_ps = []
bi_avg_ps = []
bi_std_dev_ps = []
bi_flowStart = []
bi_flowEnd = []
bi_flowDuration = []
bi_min_piat = []
bi_max_piat = []
bi_avg_piat = []
bi_std_dev_piat = []
f_pktTotalCount = []
f_octetTotalCount = []
f_min_ps = []
f_max_ps = []
f_avg_ps = []
f_std_dev_ps = []
f_flowStart = []
f_flowEnd = []
f_flowDuration = []
f_min_piat = []
f_max_piat = []
f_avg_piat = []
f_std_dev_piat = []
b_pktTotalCount = []
b_octetTotalCount = []
b_min_ps = []
b_max_ps = []
b_avg_ps = []
b_std_dev_ps = []
b_flowStart = []
b_flowEnd = []
b_flowDuration = []
b_min_piat = []
b_max_piat = []
b_avg_piat = []
b_std_dev_piat = []


def get_input():
    input_var = input("Enter 1 for individual graphs, 2 for overlapping graphs or 3 for 3x3 graphs: ")
    print("you entered " + input_var)

    return input_var


def get_colour(packet, max_value):
    if int(float(packet)) >= int(float(max_value) / 2):
        colour = 'red'
    elif int(float(packet)) < int(float(max_value) / 2):
        colour = 'green'
    else:
        colour = 'blue'

    return colour


def main():

    input_type = get_input()
    start = timeit.default_timer()

    # replace NaN values with 0
    df = pd.read_csv("results.csv")
    df.replace(np.nan, 0, inplace=True)

    df.to_csv('results2.csv', index=False, header=True)
    with open('results2.csv', 'r') as csv_file:

        # bar_chart = pygal.HorizontalStackedBar()
        bar_chart= pygal.HorizontalLine()
        # reading each line in json file and loading in each column
        # for info on the IPFIX values
        # https://www.iana.org/assignments/ipfix/ipfix.xhtml
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = 0
        for col in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                rows += 1
                numID.append(col[0])
                flowID.append(col[1])
                bwdPktID.append(col[2])
                srcIP.append(col[3])
                srcPort.append(col[4])
                dstIP.append(col[5])
                dstPort.append(col[6])
                proto.append(col[7])
                bi_pktTotalCount.append(col[8])
                bi_octetTotalCount.append(col[9])
                bi_min_ps.append(col[10])
                bi_max_ps.append(col[11])
                bi_avg_ps.append(col[12])
                bi_std_dev_ps.append(col[13])
                bi_flowStart.append(col[14])
                bi_flowEnd.append(col[15])
                bi_flowDuration.append(col[16])
                bi_min_piat.append(col[17])
                bi_max_piat.append(col[18])
                bi_avg_piat.append(col[19])
                bi_std_dev_piat.append(col[20])
                f_pktTotalCount.append(col[21])
                f_octetTotalCount.append(col[22])
                f_min_ps.append(col[23])
                f_max_ps.append(col[24])
                f_avg_ps.append(col[25])
                f_std_dev_ps.append(col[26])
                f_flowStart.append(col[27])
                f_flowEnd.append(col[28])
                f_flowDuration.append(col[29])
                f_min_piat.append(col[30])
                f_max_piat.append(col[31])
                f_avg_piat.append(col[32])
                f_std_dev_piat.append(col[33])
                b_pktTotalCount.append(col[34])
                b_octetTotalCount.append(col[35])
                b_min_ps.append(col[36])
                b_max_ps.append(col[37])
                b_avg_ps.append(col[38])
                b_std_dev_ps.append(col[39])
                b_flowStart.append(col[40])
                b_flowEnd.append(col[41])
                b_flowDuration.append(col[42])
                b_min_piat.append(col[43])
                b_max_piat.append(col[44])
                b_avg_piat.append(col[45])
                b_std_dev_piat.append(col[46])

        # plt.rcdefaults()
        objects = ('pktTotCount', 'octTotCount', 'flowDur', 'avg_piat', 'avg_ps')
        y_pos = np.arange(len(objects))*0.6

        # print(b_pktTotalCount)
        # finding max values
        maxpktCountDataF = (max(f_pktTotalCount))
        maxpktCountDataB = (max(b_pktTotalCount))
        maxoctoCountDataF =(max(f_octetTotalCount))
        maxoctoCountDataB =(max(b_octetTotalCount))
        maxdurationF =(max(f_flowDuration))
        maxdurationB = (max(b_flowDuration))
        maxpiatF = (max(f_avg_piat))
        maxpiatB = (max(b_avg_piat))
        maxpsF = (max(f_avg_ps))
        maxpsB = (max(b_avg_ps))

        # plot both graphs at same time
        # loop for amount of flows

        print("Currently Processing the data...")
        print("We are generating your graphs...")
        print("...")
        row_amt = 0
        if input_type == "1" or input_type == "2":
            row_amt = rows
        elif input_type == "3":
            row_amt = 9

        for i in range(row_amt):

            # negative values
            f_pktTotal = -int(float(f_pktTotalCount[i])*10)
            f_octTotal = -int(float(f_octetTotalCount[i])/100)
            f_duration = -int((float(f_flowDuration[i])) * 100)
            f_piatavg = -int((float(f_avg_piat[i])) * 100)
            f_pktSize = -int((float(f_avg_ps[i]))*10)

            # positive values
            b_pktTotal = int(float(b_pktTotalCount[i])*10)
            b_octTotal = (int(float(b_octetTotalCount[i])/100))
            b_duration = int((float(b_flowDuration[i])) * 100)
            b_piatavg = int((float(b_avg_piat[i])) * 100)
            b_pktSize = int((float(b_avg_ps[i]))*10)

            performanceNeg = [f_pktTotal, f_octTotal, f_duration, f_piatavg, f_pktSize]
            performancePos = [b_pktTotal, b_octTotal, b_duration, b_piatavg, b_pktSize]

            # fontsize of axis
            plt.rcParams['xtick.labelsize'] = 14
            plt.rcParams['ytick.labelsize'] = 14

            # pygal plotting
            bar_chart.add('Forward', performanceNeg)  # could use flow ID
            bar_chart.add('Backward', performancePos)  # could use flow ID
            bar_chart.x_labels = map(str, range(7))  # put in axis values

            colour1 = get_colour(f_pktTotalCount[i], maxpktCountDataF)
            colour1a = get_colour(b_pktTotalCount[i], maxpktCountDataB)
            colour2 = get_colour(f_octetTotalCount[i], maxoctoCountDataF)
            colour2a = get_colour(b_octetTotalCount[i], maxoctoCountDataB)
            colour3 = get_colour(f_flowDuration[i], maxdurationF)
            colour3a = get_colour(b_flowDuration[i], maxdurationB)
            colour4 = get_colour(f_avg_piat[i], maxpiatF)
            colour4a = get_colour(b_avg_piat[i], maxpiatB)
            colour5 = get_colour(f_avg_ps[i], maxpsF)
            colour5a = get_colour(b_avg_ps[i], maxpsB)

            if input_type == "1":

                plt.rcParams['figure.figsize'] = 5,5

                set_colors = [colour1, colour2, colour3, colour4, colour5]
                set_colorsa = [colour1a, colour2a, colour3a, colour4a, colour5a]
                alphaamt = 0.5
                posamt = 51000
                negamt = -50000
                stepamt = 10000

                plt.barh(y_pos, performancePos, height=0.5, align='center', alpha=alphaamt, color=set_colors)
                plt.barh(y_pos, performanceNeg, height=0.5, align='center', alpha=alphaamt, color=set_colorsa)

                plt.axvline(linewidth=0.1, color='black')
                plt.xticks(rotation=90)

                plt.yticks(y_pos, objects)
                plt.xticks(np.arange(negamt, posamt, step=stepamt))
                plt.xlabel('Range', fontsize=16)
                plt.ylabel('Flow Features', fontsize=16)
                plt.title('Flow ID: ' + str(numID[i]))
                # if input_type == "1":
                plt.show()

                # stop = timeit.default_timer()
                #
                # print('Time taken: ', (stop - start) / 60)

            elif input_type == "2":

                # set_colors = [colour1, colour2, colour3, colour4, colour5]
                # set_colorsa = [colour1a, colour2a, colour3a, colour4a, colour5a]

                set_colors = "red"
                set_colorsa = "red"

                alphaamt = 0.025
                posamt = 51000
                negamt = -50000
                stepamt = 10000

                plt.rcParams['figure.figsize'] = 5, 5

                plt.barh(y_pos, performancePos, height=0.5, align='center', alpha=alphaamt, color=set_colors)
                plt.barh(y_pos, performanceNeg, height=0.5, align='center', alpha=alphaamt, color=set_colorsa)

                plt.axvline(linewidth=0.1, color='black')
                plt.xticks(rotation=90)

                plt.yticks(y_pos, objects)
                plt.xticks(np.arange(negamt, posamt, step=stepamt))
                plt.xlabel('Range', fontsize=16)
                plt.ylabel('Flow Features', fontsize=16)
                plt.title('Number of overlapping flows: ' + str(632)) #+ str(numID[i]))

                # if int(numID[i]) == 100:
                #     plt.show()
                #     exit(1)


                print(str(numID[i]))
                # plt.show()

            elif input_type == "3":

                plt.subplot(3, 3, i + 1) # generating multiple per page - comment it out if you want lots on one place
                set_colors = [colour1, colour2, colour3, colour4, colour5]
                set_colorsa = [colour1a, colour2a, colour3a, colour4a, colour5a]
                alphaamt = 0.5
                posamt = 51000
                negamt = -50000
                stepamt = 25000

                plt.barh(y_pos, performancePos, height=0.5, align='center', alpha=alphaamt, color=set_colors)
                plt.barh(y_pos, performanceNeg, height=0.5, align='center', alpha=alphaamt, color=set_colorsa)

                plt.axvline(linewidth=0.1, color='black')
                plt.xticks(rotation=90)
                plt.gca().axes.get_xaxis().set_visible(False)
                plt.gca().axes.get_yaxis().set_visible(False)
                if i == 0 or i == 3 or i==6:
                    plt.gca().axes.get_yaxis().set_visible(True)
                    plt.yticks(y_pos, objects)
                    if i==3:
                        plt.ylabel('Flow Features', fontsize=16)
                if i == 6 or i == 7 or i == 8:
                    plt.gca().axes.get_xaxis().set_visible(True)
                    if i == 7:
                        plt.xlabel('Range', fontsize=16)
                plt.xticks(np.arange(negamt, posamt, step=stepamt))
                plt.title('Flow ID: ' + str(numID[i]))


        #  # pygal plotting
        # print("Processing complete")
        #
        # bar_chart.render_to_file('bar_chart2.svg')
        #
        if input_type == "2" or input_type == "3":
            plt.show()
        # stop = timeit.default_timer()
        #
        # print('Time taken: ', (stop - start)/60)

main()
