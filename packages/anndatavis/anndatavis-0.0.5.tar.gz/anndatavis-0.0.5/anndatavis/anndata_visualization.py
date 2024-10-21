import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import ipywidgets as widgets
import scipy
import anndata as ad
from PIL import Image, ImageDraw, ImageFont


#category_colors_dict: dictionary from column to dict of {value:color}, for instance category_colors_dict = {'condition': {'control':'green', 'case':'red'}}
#numeric_crange_dict: dictionary from column to range for colorbar, for instance numeric_crange_dict = {'score': (0,1)}


#TODO: consider using multiple selection widgets for genes https://gist.github.com/MattJBritton/9dc26109acb4dfe17820cf72d82f1e6f


class AnnDataVis:
    def __init__(self, anndata,
                 panels=1,
                 embed = None,
                 color_by = None, 
                 category_colors_dict = None,
                 category_legend_order_dict = None,
                 numeric_crange_dict = None,
                 numeric_colorscale_dict = None,
                 genes=None,
                 genes_use_raw = False, 
                 genes_layer = None,
                 point_size=1,
                 max_point_size=10,
                 fig_size=500,
                 click_callback = None,
                 hover_text_fields = None):
        self.anndata = anndata
        self.panels = panels
        self.embeds = self._list_embeds(anndata, maxdim=4)
        assert len(self.embeds)>0, "Must have at least one 'X_' entry in obsm"
        self.cols = list(anndata.obs.columns)

        self.genes = None
        if genes is not None:
            if type(genes)==list:
                self.genes = {g:g for g in genes}
            elif type(genes)==dict:
                self.genes = genes
            else:
                print('Error: genes should be list or dict')

        self.genes_use_raw = genes_use_raw
        self.category_colors_dict = category_colors_dict
        self.category_legend_order_dict = category_legend_order_dict
        self.numeric_crange_dict = numeric_crange_dict
        self.numeric_colorscale_dict = numeric_colorscale_dict
        self.panel_labels = [{} for i in range(panels)]
        self.genes_layer = genes_layer
        self.click_callback = click_callback
        self.hover_text_fields = hover_text_fields
        self.panels_vis_mask = [None] * panels
        self.vis_mask_opacity_factor = 0.05
        self.selected_pts = None

        default_embed = self.embeds[0]
        if embed is not None:
            if embed in self.embeds:
                default_embed = embed
            else:
                print(f'no X_{embed} in obsm. Defaulting to {self.embeds[0]}')
    
        
        default_color_by = [self.cols[0]]*panels
        self.color_opts = {c:c for c in self.cols}
        if self.genes is not None:
            self.color_opts.update(self.genes)

        if color_by is not None:
            color_by_l = [color_by] if type(color_by)!=list else color_by
            for i, color_by in enumerate(color_by_l):
                if color_by in self.color_opts:
                    default_color_by[i] = color_by
                else:
                    print(f'{color_by} is not in columns. Defaulting to {self.cols[0]}')
    
        self.ui = self._make_ui(default_embed, default_color_by, fig_size, point_size, max_point_size)
        self._update_graph_emb(dict(owner=self.dd_emb))
        for i in range(self.panels):
            self._update_graph_clr(i)
        
    def _make_ui(self, default_embed, default_color_by, fig_size, point_size, max_point_size):
        self.dd_emb = widgets.Dropdown(
            options=self.embeds,
            value=default_embed,
            description='Embedding:',
            disabled=False,
        )
        self.sld_pointsize = widgets.IntSlider(
            min=1,
            max=max_point_size,
            value=point_size,
            description='Pt.size',
        )

        self.dd_emb.observe(self._update_graph_emb, names="value")
        self.sld_pointsize.observe(self._update_point_size, names="value")

        self.dd_colors=[]
        self.ck_geneuseraws=[]
        self.ck_showlabels=[]
        self.acc_options=[]
        self.figwids=[]
        self.hover_text = []
        
        for i in range(self.panels):

            dd_color = widgets.Dropdown(
                options=self.color_opts,
                value= default_color_by[i],
                #description='Color:',
                disabled=False,
                layout=widgets.Layout(width='%dpx' % (3*fig_size//4))
            )
            dd_color.observe(self._cb_update_graph_clr_dd_color, names="value")
            self.dd_colors.append(dd_color)

            ck_geneuseraw = widgets.Checkbox(
                                value=self.genes_use_raw,
                                description='R',
                                disabled=True,
                                layout=widgets.Layout(width='%dpx' % (fig_size//6))
                                )
            ck_geneuseraw.observe(self._cb_update_graph_clr_ck_usegeneraw, names="value")
            self.ck_geneuseraws.append(ck_geneuseraw)

            ck_showlabels = widgets.Checkbox(
                                value=True,
                                description='A',
                                disabled=False,
                                layout=widgets.Layout(width='%dpx' % (fig_size//6))
                                )

            ck_showlabels.observe(self._cb_update_graph_showlabels, names="value")
            self.ck_showlabels.append(ck_showlabels)

            acc_opt = widgets.Accordion(children=[widgets.VBox([ck_geneuseraw, ck_showlabels])], titles=['Options'],
                                        layout=widgets.Layout(width='%dpx' % (1*fig_size//4), height='2-px'))
            self.acc_options.append(acc_opt)


            scatter_trace = go.Scattergl(x=[0], y=[0], mode='markers', text=[''], hoverinfo='text', visible=True,
                               marker=dict(color=[0], colorscale='Viridis', line_width=0, size=point_size))
                
            colorbar_trace  = go.Scatter(x=[None], y=[None], mode='markers', visible=False, 
                                         marker=dict(colorscale='Viridis', showscale=True,cmin=-1, cmax=1,
                                                     colorbar=dict(thickness=10, outlinewidth=2, outlinecolor='rgba(0,0,0,255)', tickfont=dict(color='rgba(128,128,128,255)'),
                                                                   #tickmode="array", tickvals=[2, 50, 100], ticktext=["2", "50", "100"], 
                                                                   x=0.0, y=0.5)),
                                         hoverinfo='none')

            anns_trace = go.Scatter(
                x=[0],
                y=[0],
                xaxis='x2',
                yaxis='y2',
                mode='markers+text',
                text=['TEST'],
                textposition='middle right',
                textfont=dict(color='white', size=10),
                marker=dict(size=15,
                            color=['#ff0000'],
                            symbol='square'),
                showlegend=False,
                hoverinfo='skip')
            
            select_trace = go.Scattergl(x=[0], y=[0], mode='markers', text=[''], hoverinfo='text', visible=False,
                               marker=dict(symbol='square-open', color=[0], colorscale='Reds', line_width=1, size=20))

            g = go.FigureWidget(data=[scatter_trace, colorbar_trace, anns_trace, select_trace],
                            layout=go.Layout(autosize=False,    width=fig_size,    height=fig_size,   showlegend=False,
                                             margin=dict(l=2 if i==0 else 0, r=2, b=2, t=2,pad=0 ),    paper_bgcolor="white", plot_bgcolor="rgba(0, 0, 0, 255)",
                                             xaxis = go.layout.XAxis(showticklabels=False, showgrid=False, zeroline=False),
                                             yaxis = go.layout.YAxis(showticklabels=False, showgrid=False, zeroline=False),
                                             dragmode = 'pan',
                                             xaxis2=dict(
                                                domain=[0, 0.2],
                                                anchor='x2',
                                                showticklabels=False,
                                                range=(0,1),
                                                showgrid=False, visible=False,
                                                fixedrange =True),
                                             yaxis2=dict(
                                                domain=[0, 1],
                                                anchor='y2',
                                                showticklabels=False,
                                                range=(0,1),
                                                showgrid=False, visible=False,
                                                fixedrange =False)))
            g.layout.on_change(self._handle_zoom, 'xaxis.range', 'yaxis.range')
            g._config = dict(scrollZoom=True)
            
            self.figwids.append(g)
            self.hover_text.append([])
        
        self.continues_colorscale = self.figwids[0].data[0].marker.colorscale

        for fw in self.figwids:
            fw.data[0].on_click(self._click_cb_internal)


        panels = [widgets.VBox([
            widgets.HBox([self.dd_colors[i], 
                          #self.ck_geneuseraws[i],
                          #self.ck_showlabels[i],
                          #self.acc_options[i],
                  ]),
            self.figwids[i]
        ])
        for i in range(len(self.figwids))]
        
        return widgets.VBox([
            widgets.HBox([
                self.dd_emb,
                self.sld_pointsize]),
            widgets.HBox(panels)
        ])
            

    def _update_point_size(self, change):
        sz = self.sld_pointsize.value
        for i in range(len(self.figwids)):
            self.figwids[i].data[0].marker.update({'size':sz})
    
    def _update_graph_emb(self, change):
        embval = self.dd_emb.value
        if embval.find(':')>0:
            embval = embval.split(':')
            embkey = 'X_'+embval[0]
            embdim0 = int(embval[1].split(',')[0])
            embdim1 = int(embval[1].split(',')[1])
        else:
            embkey = 'X_'+embval
            embdim0 = 0
            embdim1 = 1
        emb = self.anndata.obsm[embkey]
        x = emb[:,embdim0]
        y = emb[:,embdim1]
        for fw in self.figwids:
            fw.data[0].update({'x':x, 'y': y})
        self.curr_x = x
        self.curr_y = y
        
    def _cb_update_graph_clr_dd_color(self, change):
        panel_idx = self.dd_colors.index(change['owner'])
        self._update_graph_clr(panel_idx)

    def _cb_update_graph_clr_ck_usegeneraw(self, change):
        panel_idx = self.ck_geneuseraws.index(change['owner'])
        self._update_graph_clr(panel_idx)


    def _cb_update_graph_showlabels(self, change):
        panel_idx = self.ck_showlabels.index(change['owner'])
        self._update_graph_clr(panel_idx)

    def _get_color_vals(self, color_by, use_raw):
        #check if color is based on obs (cols) or gene.
        if color_by in self.cols:
            clr_vals = self.anndata.obs[color_by]
            if not clr_vals.dtype=='category' and not clr_vals.dtype=='bool' and not clr_vals.dtype=='object':
                clr_vals = clr_vals.values
            is_gene = False
        elif self.genes is not None:
            gene_idx = self.anndata.var_names.get_loc(color_by)
            if self.genes_layer is None:
                vals_mat = self.anndata.raw.X if use_raw else self.anndata.X
            else:
                vals_mat = self.anndata.layers[self.genes_layer]
            gene_vals = vals_mat[:,gene_idx]
            if scipy.sparse.issparse(gene_vals)   :
                gene_vals = gene_vals.todense().getA()
            clr_vals = gene_vals.flatten()
            is_gene = True
        else:
            clr_vals = None
            is_gene = None
        return clr_vals, is_gene
    
    
    def _update_graph_clr(self, panel_idx):
        color_by = self.dd_colors[panel_idx].value
        use_raw = self.ck_geneuseraws[panel_idx].value
        clr_vals, is_gene = self._get_color_vals(color_by, use_raw)
        if clr_vals is None:
            print('Can not set with %s' % color_by)
            return

        #handle category or boolean values
        if clr_vals.dtype=='category' or clr_vals.dtype=='bool' or clr_vals.dtype=='object':
            #categorical, boolean or object
            if clr_vals.dtype=='category':
                clr_cats = clr_vals.cat.categories
                clr_idx = clr_vals.cat.codes.values
                max_clr_idx = clr_idx.max()
            if clr_vals.dtype=='bool':
                clr_cats = ['False', 'True']
                clr_idx = clr_vals.to_numpy().astype(int)
                max_clr_idx = 1
            if clr_vals.dtype=='object':
                #try to convert to categorical. TODO: check if possible
                all_str = np.array([type(e)==str for e in clr_vals]).all()
                if all_str:
                    clr_vals = clr_vals.astype("category")
                    clr_cats = clr_vals.cat.categories
                    clr_idx = clr_vals.cat.codes.values
                    max_clr_idx = clr_idx.max()
                else:
                    print(f'Some values in the field {color_by} of type object could not be converted to string.')
                    clr_cats = ['UNDEFINED']
                    clr_idx = np.zeros(len(clr_vals))
                    max_clr_idx=0
                
            show_labels = self.ck_showlabels[panel_idx].value
                
            #convert clr_idx (0,1,...n-1) to colors and labels
            if max_clr_idx==0:
                #one value across all data
                clr_to_use = clr_idx
                clr_scale = [(0,'#ff00ff')]
                clr_labels = [(0,clr_cats[0])]
            else:
                #normalize to values in range [0,1]
                clr_to_use = clr_idx/(max_clr_idx)
                
                if self.category_colors_dict is not None and color_by in self.category_colors_dict:
                    #assign colors from provided dictionary self.category_colors_dict[color_by]={value0:color0, value1:color1...}
                    cat2color_map = self.category_colors_dict[color_by]
                    colors = [cat2color_map[c] for c in clr_cats]
                    clr_scale = [(i/max_clr_idx, colors[i]) for i in range(max_clr_idx+1)]
                else:
                    #assign colors from predefined colormaps
                    colors = px.colors.qualitative.T10 if max_clr_idx<=7 else px.colors.qualitative.Alphabet
                    clr_scale = [(i/max_clr_idx, colors[i%len(colors)]) for i in range(max_clr_idx+1)]
                
                clr_labels = [(i/max_clr_idx, clr_cats[i]) for i in range(max_clr_idx+1)]
                #sort by size
                #clr_vals.value_counts()

            hover_text = clr_vals.values
            colorbar_vis = False
            colorbar_max = 1
            colorbar_min = -1
        else:
            #numeric
            clr_to_use = clr_vals
            
            if self.numeric_colorscale_dict is not None and color_by in self.numeric_colorscale_dict:
                clr_scale = self.numeric_colorscale_dict[color_by]
            else:
                clr_scale = 'Reds' if is_gene else self.continues_colorscale
            
            hover_text = [str(v) for v in clr_vals]
            colorbar_vis = True
            if self.numeric_crange_dict is not None and color_by in self.numeric_crange_dict:
                colorbar_min = self.numeric_crange_dict[color_by][0]
                colorbar_max = self.numeric_crange_dict[color_by][1]
                clr_to_use = np.clip(clr_to_use, a_min=colorbar_min, a_max=colorbar_max)
            else:            
                colorbar_max = clr_to_use.max()
                colorbar_min = clr_to_use.min()
            clr_labels = None
            show_labels = False
        
        self.figwids[panel_idx].layout.annotations = []
        self.ck_geneuseraws[panel_idx].disabled = is_gene
        self.figwids[panel_idx].data[0].marker.update({'color':clr_to_use, 'colorscale': clr_scale})
        
        #store hover text (updated later)
        self.hover_text[panel_idx] = hover_text

        #update colorbar
        self.figwids[panel_idx].data[1].update({'visible': colorbar_vis, 'marker': {'cmax': colorbar_max, 'cmin': colorbar_min, 'colorscale': clr_scale}})

        #update legend labels
        if clr_labels is not None:
            #optional reorder of legend
            if self.category_legend_order_dict is not None and color_by in self.category_legend_order_dict:
                legend_order = self.category_legend_order_dict[color_by]
                labels = [clr_labels[i][1] for i in range(len(clr_labels))]
                labels_index = [labels.index(lbl) for lbl in legend_order]
                legend_lbl2color = {clr_labels[i][1]:clr_scale[i][1] for i in labels_index}
            else:
                legend_lbl2color = {clr_labels[i][1]:clr_scale[i][1] for i in range(len(clr_labels))}
            self.panel_labels[panel_idx] = legend_lbl2color
        else:
            self.panel_labels[panel_idx] = {}
            
        self.figwids[panel_idx].data[2].visible = show_labels
        if show_labels:
            anns_y0 = 0.03
            anns_dy = 0.03
            anns_x0 = 0.01
            self.figwids[panel_idx].data[2].visible = False
            #annotations are slower to show, limited to squares, and not clickable. See alternative below using scatter plot inside insets.
            anns_on_points = False
            anns_x = []
            anns_y = []
            anns_txt = []
            anns_clr = []
            for i,lbl in enumerate(list(self.panel_labels[panel_idx].keys())):
                if anns_on_points:
                    v = clr_labels[i][0]
                    ann_x = self.curr_x[clr_to_use==v].mean()
                    ann_y = self.curr_y[clr_to_use==v].mean()
                    xref = "x"
                    yref = "y"
                else:
                    ann_x = anns_x0
                    ann_y = 1-anns_y0-i*anns_dy
                    xref = "paper"
                    yref = "paper"
                anns_x.append(ann_x)
                anns_y.append(ann_y)
                anns_txt.append(lbl)
                anns_clr.append(self.panel_labels[panel_idx][lbl])
                continue
                self.figwids[panel_idx].add_annotation (x=ann_x, y=ann_y, xref=xref, yref=yref, text=clr_labels[i][1], ax=0, ay=0,
                                                       font=dict(family="Ariel", size=12, color="#ffffff"),
                                                       align="left", xanchor="left", yanchor="bottom", bordercolor="#ffffff", borderwidth=1, borderpad=1, bgcolor=clr_scale[i][1], opacity=0.8)
                
            self.figwids[panel_idx].data[2].x=anns_x
            self.figwids[panel_idx].data[2].y=anns_y
            self.figwids[panel_idx].data[2].text=anns_txt
            self.figwids[panel_idx].data[2].marker.color = anns_clr
            self.figwids[panel_idx].data[2].visible = True
        else:
            self.figwids[panel_idx].data[2].visible = False

        #update hover text for the panel
        hover_text = [f'<b>{idd}<\b><br> {color_by}: {s}' for idd,s in zip(list(self.anndata.obs.index), self.hover_text[panel_idx])]
        if self.hover_text_fields is not None:
            def dict2str(d):
                return '<br>'.join([f' {k}:\t{v}' for k,v in d.items()])
            hover_text_fields = [f for f in self.hover_text_fields if f!=color_by]
            hover_text_from_other_flds = [dict2str(a.to_dict()) for _,a in self.anndata.obs[hover_text_fields].iterrows()]
            hover_text = [t1+'<br>'+t2 for t1,t2 in zip(hover_text, hover_text_from_other_flds)]
        self.figwids[panel_idx].data[0].update({'text':hover_text})

                    
            
            
        
    
    def _handle_zoom(self, layout, x_range, y_range):
        def dummy_handle_zoom(layout_, x_range, y_range):
            #panel_idx_ = [fw.layout for fw in self.figwids].index(layout_)
            #print('on tmp from %d' % panel_idx_)
            pass
        
        panel_idx = [fw.layout for fw in self.figwids].index(layout)
        #print(panel_idx)
        for i in range(len(self.figwids)):
            if i!=panel_idx:
                self.figwids[i].layout.on_change(dummy_handle_zoom, 'xaxis.range', 'yaxis.range')
                self.figwids[i].update_layout(dict(xaxis=dict(range=x_range), yaxis=dict(range=y_range)))
                self.figwids[i].layout.on_change(self._handle_zoom, 'xaxis.range', 'yaxis.range')


    def _list_embeds(self, anndata, maxdim=2):
        embeds = []
        for k in anndata.obsm.keys():
            if k.startswith('X_'):
                d = anndata.obsm[k].shape[1]
                if d==2:
                    embeds.append(k[2:])
                if d>2:
                    for d1 in range(0, maxdim):
                        for d2 in range(d1+1, maxdim):
                            embeds.append(f'{k[2:]}:{d1},{d2}')
        return embeds
                    
    def show(self):
        return self.ui

    def add_genes(self, genes):
        for gene in genes:
            if self.genes is None:
                self.genes = [gene]

            elif gene not in self.genes:
                self.genes.append(gene)

        for dd_color in self.dd_colors:
            dd_color.unobserve(self._cb_update_graph_clr_dd_color, names="value")
            curr_idx = dd_color.index
            dd_color.index = None
            opt_lst = list(dd_color.options)
            for gene in genes:
                if gene not in dd_color.options:
                    opt_lst.append(gene)
            dd_color.options = tuple(opt_lst)
            dd_color.index = curr_idx
            dd_color.observe(self._cb_update_graph_clr_dd_color, names="value")

    def set_color_in_panel(self, panel_idx, color_by):
        if panel_idx>=self.panels:
            return
        
        self.dd_colors[panel_idx].value = color_by
        
    def set_click_callback(self, click_cb):
        self.click_callback = click_cb

    def _update_opacity(self, panel_idx):
        if self.panels_vis_mask[panel_idx] is None:
            opacity = np.ones(len(self.anndata))
        else:
            opacity = self.vis_mask_opacity_factor+(1.0-self.vis_mask_opacity_factor)*self.panels_vis_mask[panel_idx].astype(float)
        self.figwids[panel_idx].data[0].marker.update({'opacity':opacity})

    #set visibility mask. vis_mask is a boolean vector of size as input, indiciating which points to show. Can update one panel or all.
    def set_visibility_mask(self, vis_mask, panel=None):
        if panel is None:
            for i in range(self.panels):
                self.panels_vis_mask[i] = vis_mask
                self._update_opacity(i)
        else:
            self.panels_vis_mask[panel] = vis_mask
            self._update_opacity(panel)

    #set visibility mask. vis_mask is a boolean vector of size as input, indiciating which points to show. Can update one panel or all.
    def clear_visibility_mask(self, panel=None):
        if panel is None:
            for i in range(self.panels):
                self.panels_vis_mask[i] = None
                self._update_opacity(i)
        else:
            self.panels_vis_mask[panel] = None
            self._update_opacity(panel)

    def _update_selected_points_view(self):
        for i in range(len(self.figwids)):
            if self.selected_pts is None:
                self.figwids[i].data[3].visible=False
            else:
                self.figwids[i].data[3].x=self.figwids[i].data[0].x[self.selected_pts]
                self.figwids[i].data[3].y=self.figwids[i].data[0].y[self.selected_pts]
                self.figwids[i].data[3].visible=True

    def _click_cb_internal(self, figwid, pts, clickstate):
        self.selected_pts = pts.point_inds
        #print(self.selected_pts)
        self._update_selected_points_view()
        if self.click_callback is not None:
            self.click_callback(figwid, pts, clickstate)

    def get_selected_points(self):
        return self.selected_pts
    
    def clear_selection(self):
        self.selected_pts = None
        self._update_selected_points_view()

    def set_selection(self, selected_pts):
        self.selected_pts = selected_pts
        self._update_selected_points_view()
    

    def save_panel_to_file(self, panel_idx, fname, header_from_color_select=True, header_font_size=14):
        #make sure background is black
        self.figwids[panel_idx].layout.update(dict(plot_bgcolor='rgba(0,0,0,255)'))
        #save file
        self.figwids[panel_idx].write_image(fname)
        #add header
        if header_from_color_select:
            orig_image = Image.open(fname)
            top_margin = 20+header_font_size
            new_image = Image.new(orig_image.mode, (orig_image.width, orig_image.height+top_margin), color='white')
            new_image.paste(orig_image, (0,top_margin,orig_image.width, orig_image.height+top_margin))
            draw = ImageDraw.Draw(new_image)
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", header_font_size)
            text = self.dd_colors[panel_idx].value
            text_bbox = font.getbbox(text)  
            text_w = text_bbox[2]-text_bbox[0]
            position = (new_image.size[0]/2-text_w/2, 10)
            draw.text(position, text, font=font, fill=(0,0,0,255))
            # Save or display the modified image
            new_image.save(fname)


#show anndata with the visualizer
def show_anndata(anndata, panels=1, color_by=None, embed=None, genes=None, genes_use_raw = False, genes_layer = None, fig_size=500, 
                 category_colors_dict=None, category_legend_order_dict=None,
                 point_size=1, max_point_size=10, numeric_crange_dict=None, numeric_colorscale_dict=None, click_callback=None, hover_text_fields=None):
    annvis = AnnDataVis(anndata, panels=panels, color_by=color_by, embed=embed, genes=genes, genes_use_raw=genes_use_raw, genes_layer=genes_layer,
                        fig_size=fig_size, category_colors_dict=category_colors_dict, category_legend_order_dict=category_legend_order_dict,
                        point_size=point_size, max_point_size=max_point_size,
                        numeric_crange_dict = numeric_crange_dict, numeric_colorscale_dict = numeric_colorscale_dict,  click_callback = click_callback,
                        hover_text_fields = hover_text_fields)
    return annvis.ui
    
            


