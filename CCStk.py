#!/usr/bin/env python
# coding: utf-8

# In[85]:


import tkinter as tk


# In[86]:


# Theoretical storage calculations

def storage():
    """Calculate the effective storage capacity"""
    porv = float(ent_bulk_vol.get())*float(ent_ntg.get())/100*float(ent_poro.get())/100*float(ent_trap.get())/100
    eff_fac = (float(ent_fm_comp.get())+float(ent_fld_comp.get()))*(float(ent_pmax.get())-float(ent_pinit.get()))
    stor_cap = porv*float(ent_co2_dens.get())
    eff_cap = stor_cap*eff_fac
    lbl_result["text"] = f"{round(eff_cap, 0)} kg"


# In[87]:


# Set up window properties
window = tk.Tk()
window.title("Carbon Storage Calculator")
window.resizable(width=False, height=False)


# In[88]:


# Set up input boxes and units

frm_input = tk.Frame(master=window)

# Bulk volume
ent_bulk_vol = tk.Entry(master=frm_input, width=10)
units_bulk_vol = tk.Label(master=frm_input, text="m3")
lbl_bulk_vol = tk.Label(master=frm_input, text="Bulk Volume")

# Net-to-Gross
ent_ntg = tk.Entry(master=frm_input, width=10)
units_ntg = tk.Label(master=frm_input, text="%")
lbl_ntg = tk.Label(master=frm_input, text="NTG")

# Porosity
ent_poro = tk.Entry(master=frm_input, width=10)
units_poro = tk.Label(master=frm_input, text="%")
lbl_poro = tk.Label(master=frm_input, text="Porosity")

# Trap proportion of total volume
ent_trap = tk.Entry(master=frm_input, width=10)
units_trap = tk.Label(master=frm_input, text="%")
lbl_trap = tk.Label(master=frm_input, text="Trap Proportion")

# Density of CO2
ent_co2_dens = tk.Entry(master=frm_input, width=10)
units_co2_dens = tk.Label(master=frm_input, text="kg/m3")
lbl_co2_dens = tk.Label(master=frm_input, text="CO2 Density")

# Formation compressibility
ent_fm_comp = tk.Entry(master=frm_input, width=10)
units_fm_comp = tk.Label(master=frm_input, text="1/Mpa")
lbl_fm_comp = tk.Label(master=frm_input, text="Formation Compressibility")

# Fluid compressibility
ent_fld_comp = tk.Entry(master=frm_input, width=10)
units_fld_comp = tk.Label(master=frm_input, text="1/Mpa")
lbl_fld_comp = tk.Label(master=frm_input, text="Fluid Compressibility")

# Initial pressure
ent_pinit = tk.Entry(master=frm_input, width=10)
units_pinit = tk.Label(master=frm_input, text="Mpa")
lbl_pinit = tk.Label(master=frm_input, text="Initial Pressure")

# Maximum pressure
ent_pmax = tk.Entry(master=frm_input, width=10)
units_pmax = tk.Label(master=frm_input, text="Mpa")
lbl_pmax = tk.Label(master=frm_input, text="Maximum Pressure")


# In[89]:


# Position widgets in frame

lbl_bulk_vol.grid(row=0, column=0)
ent_bulk_vol.grid(row=0, column=1, sticky="e")
units_bulk_vol.grid(row=0, column=2, sticky="w")

lbl_ntg.grid(row=1, column=0)
ent_ntg.grid(row=1, column=1, sticky="e")
units_ntg.grid(row=1, column=2, sticky="w")

lbl_poro.grid(row=2, column=0)
ent_poro.grid(row=2, column=1, sticky="e")
units_poro.grid(row=2, column=2, sticky="w")

lbl_trap.grid(row=3, column=0)
ent_trap.grid(row=3, column=1, sticky="e")
units_trap.grid(row=3, column=2, sticky="w")

lbl_co2_dens.grid(row=4, column=0)
ent_co2_dens.grid(row=4, column=1, sticky="e")
units_co2_dens.grid(row=4, column=2, sticky="w")

lbl_fm_comp.grid(row=5, column=0)
ent_fm_comp.grid(row=5, column=1, sticky="e")
units_fm_comp.grid(row=5, column=2, sticky="w")

lbl_fld_comp.grid(row=6, column=0)
ent_fld_comp.grid(row=6, column=1, sticky="e")
units_fld_comp.grid(row=6, column=2, sticky="w")

lbl_pinit.grid(row=7, column=0)
ent_pinit.grid(row=7, column=1, sticky="e")
units_pinit.grid(row=7, column=2, sticky="w")

lbl_pmax.grid(row=8, column=0)
ent_pmax.grid(row=8, column=1, sticky="e")
units_pmax.grid(row=8, column=2, sticky="w")


# In[90]:


# Calculate button and results

btn_calc = tk.Button(master=window, text="Calculate", command=storage)
lbl_result = tk.Label(master=window, text="kg")

btn_calc.grid(row=1, column=0)
lbl_result.grid(row=2, column=0)


# In[91]:


frm_input.grid(row=0, column=0, padx=10)


# In[ ]:


window.mainloop()


# In[ ]:




