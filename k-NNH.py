import time
import datetime
import math
import sys
import os
EARTH_REDIUS = 6378.137
def rad(d):
    return float(d) * 3.14 / 180.0
def get_dis(lat1, lng1, lat2, lng2) :
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

def get_delt_time(time1, time2) :
    return (time1 - time2).seconds / 3600

class Node :
    def __init__(self, id_, time_, lat_, lng_, nid_) :
        self.id_ = id_
        self.time_ = time_ 
        self.datetime_ = datetime.datetime.utcfromtimestamp(time_)
        self.lat_ = lat_ 
        self.lng_ = lng_ 
        self.nid_ = nid_ 
class Graph :
    def __init__(self, id_, nodes_) :
        self.id_ = id_
        self.nodes_ = nodes_
        self.init_node_ = nodes_[0]
        self.path_ = [nodes_[0]]
        self.distants_ = {}
        self.visited = set()
    def cal_dis(self) :
        for source in nodes_ :
            if (source.time_ < self.init_node_.time_) :
                self.init_node_ = source
            dis = []
            for target in nodes_ :
                dis.append((target, get_dis(source.lat_, source.lng_,
                                            target.lat_, target.lng_)))
            dis.sort(key = lambda item: item[1])
            self.distants_[source] = dis
    def k_NNH(self, k) :
        old_size = 0
        new_size = -1
        while (old_size != new_size) :
            old_size = len(self.path_)
            node = self.path_[-1]
            i = 0
            j = 0
            dis = self.distants_.get(node)
            while (j < k) :
                if (i >= len(dis)) :
                    break
                if (dis[i][0] in self.visited) :
                    i = i + 1
                    continue
                if (dis[i][1]/30 < get_delt_time(dis[i][0].datetime_, 
                                                 node.datetime_)) :
                    self.path_.append(dis[i][0])
                    self.visited.add(dis[i][0])
                    j = j + 1
                i = i + 1
            new_size = len(self.path_)
            return (len(self.path_), len(self.path_)/len(self.nodes_))

    def print_graph(self) :
        for (source, dis) in self.distants_.items() :
            print(source.nid_)
            for (target, d) in dis :
                print((target.nid_, d))

def read_file(date) :
    graphs_map = {}
    f = open(date + '.txt','r')
    i = 0
    for line in f.readlines() :
        if (len(line) < 10) :
            break
        args = line.split('\t')
        node = Node(args[0], 
                    time.mktime(time.strptime(args[1], "%Y-%m-%dT%H:%M:%SZ")),
                    args[2], args[3], args[4])
        if (not graphs_map.__contains__(args[0])) :
            graphs_map[args[0]] = []
        graphs_map.get(args[0]).append(node)
    return graphs_map

fo = open('result.txt','w')
ks = [1, 2, 3, 5, 10, 100]
#start_date = datetime.date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
#end_date = datetime.date(int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
start_date = datetime.date(2009, 2, 3)
end_date = datetime.date(2010, 10, 22)
for i in range((end_date - start_date).days + 1) :
    date = start_date + datetime.timedelta(days=i)
    file_name = str(date) + '.txt'
    if (not os.path.isfile(file_name)) :
        continue
    graphs_map = read_file(str(date))
    for k in ks :
        start = datetime.datetime.now()
        acc = 0;
        for (id_, nodes_) in graphs_map.items() :
            g = Graph(id_, nodes_)
            g.cal_dis()
            acc = g.k_NNH(k)[1] + acc
        end = datetime.datetime.now()
        print((date, k, acc/len(graphs_map.items()), (end-start).microseconds/1000))
        fo.write(str((date, k, acc/len(graphs_map.items()), (end-start).microseconds/1000)) + '\n')
