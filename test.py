import pandas
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.lib import grid
from rpy2.robjects.lib import ggplot2
 
## read in the distances to railroad (we calculated)
neardist = pandas.read_csv('/Users/user/Downloads/data/NearDistance.csv')
 
## convert to R dataframe, via Python Dictionary data type
neardist_dataf = {'OBAMA_SHAR':  robjects.FloatVector(neardist['OBAMA_SHAR']), 'NEAR_DIST': robjects.FloatVector(neardist['NEAR_DIST'])}
RR_distance = robjects.DataFrame(neardist_dataf)
print RR_distance.colnames
 
## we use R instance of robjects to issue R commands
## load  pre-prepared IL map data sets and print contents:
robjects.r('print(load("/Users/user/Downloads/data/IL.Rdata"))')
 
## loaded data sets can now be accessed through R handle
## note that different from R dot . is not valid for Python variable names!
IL_railroads = robjects.r('IL.railroads')
IL_final = robjects.r('IL.final')
 
## import device driver from R with importr to plot to PNG
## we can then call any function in the grdevices package
grdevices = importr('grDevices')
grdevices.png(file='/Users/user/Downloads/data/mapplot.png', width=1300, height=1000)
 
## plot the map
## note that the order matters when we add another layer in ggplot (here IL_railroads): first aes, then data, that's different from R 
## (see http://permalink.gmane.org/gmane.comp.python.rpy/2349) 
## note that we use dictionary to set the opts to be able to set options as keywords, for example legend.key.size
p_map = ggplot2.ggplot(IL_final) + \
     ggplot2.geom_polygon(ggplot2.aes(x = 'long', y = 'lat', group = 'group', color = 'ObamaShare', fill = 'ObamaShare')) + \
     ggplot2.scale_fill_gradient(high = 'blue', low = 'red') + \
     ggplot2.scale_fill_continuous(name = "Obama Vote Share") + \
     ggplot2.scale_colour_continuous(name = "Obama Vote Share") + \
     ggplot2.opts(**{'legend.position': 'left', 'legend.key.size': robjects.r.unit(2, 'lines'), 'legend.title' : ggplot2.theme_text(size = 14, hjust=0), \
                     'legend.text': ggplot2.theme_text(size = 12), 'title' : "Obama Vote Share and Distance to Railroads in IL", \
                     'plot.title': ggplot2.theme_text(size = 24), 'plot.margin': robjects.r.unit(robjects.r.rep(0,4),'lines'), \
                     'panel.background': ggplot2.theme_blank(), 'panel.grid.minor': ggplot2.theme_blank(), 'panel.grid.major': ggplot2.theme_blank(), \
                     'axis.ticks': ggplot2.theme_blank(), 'axis.title.x': ggplot2.theme_blank(), 'axis.title.y': ggplot2.theme_blank(), \
                     'axis.title.x': ggplot2.theme_blank(), 'axis.title.x': ggplot2.theme_blank(), 'axis.text.x': ggplot2.theme_blank(), \
                     'axis.text.y': ggplot2.theme_blank()} ) + \
     ggplot2.geom_line(ggplot2.aes(x='long', y='lat', group='group'), data=IL_railroads, color='grey', size=0.2) + \
     ggplot2.coord_equal()
 
p_map.plot()
 
## add the scatterplot
## define layout of subplot with viewports

vp_sub = grid.viewport(x = 0.19, y = 0.2, width = 0.32, height = 0.4)
 
p_sub = ggplot2.ggplot(RR_distance) + \
    ggplot2.aes_string(x = 'OBAMA_SHAR', y= 'NEAR_DIST') + \
    ggplot2.geom_point(ggplot2.aes(color='OBAMA_SHAR')) + \
    ggplot2.stat_smooth(color="black") + \
    ggplot2.opts(**{'legend.position': 'none'}) + \
    ggplot2.scale_x_continuous("Obama Vote Share") + \
    ggplot2.scale_y_continuous("Distance to nearest Railroad")
 
p_sub.plot(vp=vp_sub)

grdevices.dev_off()