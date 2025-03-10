import random
import json
import tkinter as tk
from tkinter import ttk
import pandas as pd
from datetime import datetime
import numpy as np

# Teams Data
teams_1950 = [
    {"name": "Alfa Romeo", "performance": 70, "budget": 1000000},
    {"name": "Ferrari", "performance": 55, "budget": 900000},
    {"name": "Talbot Lago", "performance": 50, "budget": 800000},
    {"name": "Kurtis Kraft", "performance": 40, "budget": 700000},
    {"name": "Maserati", "performance": 35, "budget": 600000},
    {"name": "Deidt", "performance": 30, "budget": 500000},
    {"name": "Simca", "performance": 20, "budget": 400000},
    {"name": "ERA", "performance": 20, "budget": 300000},
    {"name": "Alta", "performance": 20, "budget": 200000},
    {"name": "Cooper", "performance": 20, "budget": 100000},
]

teams_1951 = [
    {"name": "Alfa Romeo", "performance": 70, "budget": 1000000},
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "Kurtis Kraft", "performance": 50, "budget": 900000},
    {"name": "Sherman", "performance": 40, "budget": 800000},
    {"name": "Talbot Lago", "performance": 40, "budget": 800000},
    {"name": "BRM", "performance": 35, "budget": 700000},
    {"name": "Schraeder", "performance": 35, "budget": 700000},
    {"name": "Simca", "performance": 20, "budget": 500000},
    {"name": "Maserati", "performance": 20, "budget": 500000},
    {"name": "ERA", "performance": 20, "budget": 500000},
    {"name": "HWM", "performance": 20, "budget": 500000},
    {"name": "OSCA", "performance": 20, "budget": 500000},
    {"name": "Veritas", "performance": 20, "budget": 500000},
    {"name": "Alta", "performance": 20, "budget": 500000},
]

teams_1952 = [
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "Gordini", "performance": 50, "budget": 900000},
    {"name": "Cooper", "performance": 45, "budget": 800000},
    {"name": "Kuzma", "performance": 40, "budget": 700000},
    {"name": "Maserati", "performance": 35, "budget": 600000},
    {"name": "Kurtis Kraft", "performance": 35, "budget": 600000},
    {"name": "Connaught", "performance": 30, "budget": 500000},
    {"name": "Frazer Nash", "performance": 30, "budget": 500000},
    {"name": "Lesovsky", "performance": 30, "budget": 500000},
    {"name": "HWM", "performance": 25, "budget": 400000},
    {"name": "Simca", "performance": 25, "budget": 400000},
    {"name": "Veritas", "performance": 20, "budget": 300000},
    {"name": "AFM", "performance": 20, "budget": 300000},
    {"name": "Alta", "performance": 20, "budget": 300000},
    {"name": "Heck", "performance": 20, "budget": 300000},
    {"name": "ERA", "performance": 20, "budget": 300000},
    {"name": "OSCA", "performance": 20, "budget": 300000},
    {"name": "Aston Butterworth", "performance": 20, "budget": 300000},
    {"name": "Reif", "performance": 20, "budget": 300000},
    {"name": "Balsa", "performance": 20, "budget": 300000},
    {"name": "Nacke", "performance": 20, "budget": 300000},
    {"name": "Krakau", "performance": 20, "budget": 300000},
]

teams_1953 = [
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "Maserati", "performance": 60, "budget": 900000},
    {"name": "Kurtis Kraft", "performance": 50, "budget": 800000},
    {"name": "Gordini", "performance": 40, "budget": 700000},
    {"name": "Cooper", "performance": 30, "budget": 600000},
    {"name": "Connaught", "performance": 30, "budget": 600000},
    {"name": "HWM", "performance": 30, "budget": 600000},
    {"name": "Veritas", "performance": 30, "budget": 600000},
    {"name": "OSCA", "performance": 30, "budget": 600000},
    {"name": "Simca", "performance": 30, "budget": 600000},
    {"name": "AFM", "performance": 30, "budget": 600000},
    {"name": "Greifzu", "performance": 30, "budget": 600000},
    {"name": "Heck", "performance": 30, "budget": 600000},
    {"name": "EMW", "performance": 30, "budget": 600000},
]

teams_1954 = [
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "Mercedes", "performance": 65, "budget": 900000},
    {"name": "Maserati", "performance": 60, "budget": 800000},
    {"name": "Kurtis Kraft", "performance": 50, "budget": 700000},
    {"name": "Kuzma", "performance": 40, "budget": 600000},
    {"name": "Gordini", "performance": 30, "budget": 500000},
    {"name": "Vanwall", "performance": 30, "budget": 500000},
    {"name": "Cooper", "performance": 30, "budget": 500000},
    {"name": "Connaught", "performance": 30, "budget": 500000},
    {"name": "Lancia", "performance": 30, "budget": 500000},
    {"name": "HWM", "performance": 30, "budget": 500000},
    {"name": "Klenk", "performance": 30, "budget": 500000},
]

teams_1955 = [
    {"name": "Mercedes", "performance": 70, "budget": 1000000},
    {"name": "Ferrari", "performance": 65, "budget": 900000},
    {"name": "Maserati", "performance": 60, "budget": 800000},
    {"name": "Kurtis Kraft", "performance": 50, "budget": 700000},
    {"name": "Lancia", "performance": 40, "budget": 600000},
    {"name": "Kuzma", "performance": 30, "budget": 500000},
    {"name": "Gordini", "performance": 30, "budget": 500000},
    {"name": "Vanwall", "performance": 30, "budget": 500000},
    {"name": "Connaught", "performance": 30, "budget": 500000},
    {"name": "Cooper", "performance": 30, "budget": 500000},
]

teams_1956 = [
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "Maserati", "performance": 65, "budget": 900000},
    {"name": "Watson", "performance": 50, "budget": 800000},
    {"name": "Connaught", "performance": 45, "budget": 700000},
    {"name": "Kurtis Kraft", "performance": 40, "budget": 600000},
    {"name": "Phillips", "performance": 35, "budget": 500000},
    {"name": "Vanwall", "performance": 30, "budget": 400000},
    {"name": "Gordini", "performance": 25, "budget": 300000},
    {"name": "Cooper", "performance": 20, "budget": 200000},
    {"name": "BRM", "performance": 20, "budget": 200000},
    {"name": "Bugatti", "performance": 20, "budget": 200000},
]

teams_1957 = [
    {"name": "Maserati", "performance": 70, "budget": 1000000},
    {"name": "Vanwall", "performance": 60, "budget": 900000},
    {"name": "Ferrari", "performance": 50, "budget": 800000},
    {"name": "Salih", "performance": 35, "budget": 700000},
    {"name": "Epperly", "performance": 30, "budget": 600000},
    {"name": "Kuzma", "performance": 25, "budget": 500000},
    {"name": "Kurtis Kraft", "performance": 20, "budget": 400000},
    {"name": "Connaught", "performance": 20, "budget": 400000},
    {"name": "Cooper", "performance": 15, "budget": 300000},
    {"name": "BRM", "performance": 10, "budget": 200000},
]

teams_1958 = [
    {"name": "Vanwall", "performance": 70, "budget": 1000000},
    {"name": "Ferrari", "performance": 65, "budget": 900000},
    {"name": "Cooper Climax", "performance": 60, "budget": 800000},
    {"name": "BRM", "performance": 50, "budget": 700000},
    {"name": "Maserati", "performance": 35, "budget": 600000},
    {"name": "Lotus Climax", "performance": 30, "budget": 500000},
]

teams_1959 = [
    {"name": "Cooper Climax", "performance": 70, "budget": 1000000},
    {"name": "Ferrari", "performance": 65, "budget": 900000},
    {"name": "BRM", "performance": 50, "budget": 800000},
    {"name": "Lotus Climax", "performance": 35, "budget": 700000},
]

teams_1960 = [
    {"name": "Cooper Climax", "performance": 70, "budget": 1000000},
    {"name": "Lotus Climax", "performance": 60, "budget": 900000},
    {"name": "Ferrari", "performance": 55, "budget": 800000},
    {"name": "BRM", "performance": 30, "budget": 700000},
    {"name": "Cooper Maserati", "performance": 25, "budget": 600000},
    {"name": "Cooper Castellotti", "performance": 25, "budget": 600000},
]

teams_1961 = [
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "Lotus Climax", "performance": 60, "budget": 900000},
    {"name": "Porsche", "performance": 55, "budget": 800000},
    {"name": "Cooper Climax", "performance": 30, "budget": 700000},
    {"name": "BRM Climax", "performance": 25, "budget": 600000},
]

teams_1962 = [
    {"name": "BRM", "performance": 70, "budget": 1000000},
    {"name": "Lotus Climax", "performance": 65, "budget": 900000},
    {"name": "Cooper Climax", "performance": 60, "budget": 800000},
    {"name": "Lola Climax", "performance": 55, "budget": 700000},
    {"name": "Porsche", "performance": 50, "budget": 600000},
    {"name": "Ferrari", "performance": 50, "budget": 600000},
    {"name": "Brabham Climax", "performance": 35, "budget": 500000},
    {"name": "Lotus BRM", "performance": 35, "budget": 500000},
]

teams_1963 = [
    {"name": "Lotus Climax", "performance": 70, "budget": 1000000},
    {"name": "BRM", "performance": 60, "budget": 900000},
    {"name": "Brabham Climax", "performance": 55, "budget": 800000},
    {"name": "Ferrari", "performance": 50, "budget": 700000},
    {"name": "Cooper Climax", "performance": 45, "budget": 600000},
    {"name": "BRP BRM", "performance": 30, "budget": 500000},
    {"name": "Porsche", "performance": 25, "budget": 400000},
    {"name": "Lotus BRM", "performance": 20, "budget": 300000},
]

teams_1964 = [
    {"name": "Ferrari", "performance": 70, "budget": 1000000},
    {"name": "BRM", "performance": 65, "budget": 900000},
    {"name": "Lotus Climax", "performance": 60, "budget": 800000},
    {"name": "Brabham Climax", "performance": 55, "budget": 700000},
    {"name": "Cooper Climax", "performance": 40, "budget": 600000},
    {"name": "Brabham BRM", "performance": 25, "budget": 500000},
    {"name": "BRP BRM", "performance": 20, "budget": 400000},
    {"name": "Lotus BRM", "performance": 15, "budget": 300000},
]

teams_1965 = [
    {"name": "Lotus Climax", "performance": 70, "budget": 1000000},
    {"name": "BRM", "performance": 65, "budget": 900000},
    {"name": "Brabham Climax", "performance": 50, "budget": 800000},
    {"name": "Ferrari", "performance": 45, "budget": 700000},
    {"name": "Cooper Climax", "performance": 35, "budget": 600000},
    {"name": "Honda", "performance": 30, "budget": 500000},
    {"name": "Brabham BRM", "performance": 20, "budget": 400000},
    {"name": "Lotus BRM", "performance": 15, "budget": 300000},
]

teams_1966 = [
    {"name": "Brabham Repco", "performance": 70, "budget": 1000000},
    {"name": "Ferrari", "performance": 60, "budget": 900000},
    {"name": "Cooper Maserati", "performance": 60, "budget": 800000},
    {"name": "BRM", "performance": 50, "budget": 700000},
    {"name": "Lotus BRM", "performance": 40, "budget": 600000},
    {"name": "Lotus Climax", "performance": 30, "budget": 500000},
    {"name": "Eagle Climax", "performance": 35, "budget": 400000},
    {"name": "Honda", "performance": 30, "budget": 300000},
    {"name": "McLaren Ford", "performance": 25, "budget": 200000},
    {"name": "Brabham BRM", "performance": 20, "budget": 100000},
    {"name": "McLaren Serenissima", "performance": 20, "budget": 100000},
    {"name": "Brabham Climax", "performance": 20, "budget": 100000},
]

teams_1967 = [
    {"name": "Brabham Repco", "performance": 75, "budget": 1000000},
    {"name": "Lotus Ford", "performance": 65, "budget": 900000},
    {"name": "Cooper Maserati", "performance": 55, "budget": 800000},
    {"name": "Honda", "performance": 50, "budget": 700000},
    {"name": "Ferrari", "performance": 50, "budget": 700000},
    {"name": "BRM", "performance": 45, "budget": 600000},
    {"name": "Eagle Weslake", "performance": 40, "budget": 500000},
    {"name": "Cooper Climax", "performance": 30, "budget": 400000},
    {"name": "Lotus BRM", "performance": 30, "budget": 400000},
    {"name": "McLaren BRM", "performance": 25, "budget": 300000},
    {"name": "Brabham Climax", "performance": 20, "budget": 200000},
]

teams_1968 = [
    {"name": "Lotus Ford", "performance": 75, "budget": 1000000},
    {"name": "McLaren Ford", "performance": 65, "budget": 900000},
    {"name": "Matra Ford", "performance": 65, "budget": 800000},
    {"name": "Ferrari", "performance": 55, "budget": 700000},
    {"name": "BRM", "performance": 50, "budget": 600000},
    {"name": "Honda", "performance": 40, "budget": 500000},
    {"name": "Cooper BRM", "performance": 40, "budget": 500000},
    {"name": "Brabham Repco", "performance": 35, "budget": 400000},
    {"name": "Matra", "performance": 30, "budget": 300000},
    {"name": "McLaren BRM", "performance": 25, "budget": 200000},
]

teams_1969 = [
    {"name": "Matra Ford", "performance": 75, "budget": 1000000},
    {"name": "Brabham Ford", "performance": 65, "budget": 900000},
    {"name": "Lotus Ford", "performance": 65, "budget": 800000},
    {"name": "McLaren Ford", "performance": 55, "budget": 700000},
    {"name": "Ferrari", "performance": 40, "budget": 600000},
    {"name": "BRM", "performance": 40, "budget": 600000},
]

teams_1970 = [
    {"name": "Lotus Ford", "performance": 80, "budget": 1000000},
    {"name": "Ferrari", "performance": 75, "budget": 900000},
    {"name": "March Ford", "performance": 75, "budget": 800000},
    {"name": "Brabham Ford", "performance": 65, "budget": 700000},
    {"name": "McLaren Ford", "performance": 65, "budget": 700000},
    {"name": "BRM", "performance": 55, "budget": 600000},
    {"name": "Matra", "performance": 55, "budget": 600000},
    {"name": "Surtees Ford", "performance": 40, "budget": 500000},
]

teams_1971 = [
    {"name": "Tyrrell Ford", "performance": 80, "budget": 1000000},
    {"name": "BRM", "performance": 65, "budget": 900000},
    {"name": "Ferrari", "performance": 65, "budget": 800000},
    {"name": "March Ford", "performance": 65, "budget": 800000},
    {"name": "Lotus Ford", "performance": 55, "budget": 700000},
    {"name": "McLaren Ford", "performance": 45, "budget": 600000},
    {"name": "Matra", "performance": 45, "budget": 500000},
    {"name": "Surtees Ford", "performance": 45, "budget": 400000},
    {"name": "Brabham Ford", "performance": 40, "budget": 300000},
]

teams_1972 = [
    {"name": "Lotus Ford", "performance": 75, "budget": 1000000},
    {"name": "Tyrrell Ford", "performance": 70, "budget": 900000},
    {"name": "McLaren Ford", "performance": 70, "budget": 800000},
    {"name": "Ferrari", "performance": 60, "budget": 700000},
    {"name": "Surtees Ford", "performance": 50, "budget": 600000},
    {"name": "March Ford", "performance": 45, "budget": 500000},
    {"name": "BRM", "performance": 45, "budget": 400000},
    {"name": "Matra", "performance": 40, "budget": 300000},
    {"name": "Brabham Ford", "performance": 30, "budget": 200000},
]

teams_1973 = [
    {"name": "Lotus Ford", "performance": 75, "budget": 1000000},
    {"name": "Tyrrell Ford", "performance": 70, "budget": 900000},
    {"name": "McLaren Ford", "performance": 55, "budget": 800000},
    {"name": "Brabham Ford", "performance": 40, "budget": 700000},
    {"name": "March Ford", "performance": 35, "budget": 600000},
    {"name": "Ferrari", "performance": 35, "budget": 500000},
    {"name": "BRM", "performance": 35, "budget": 500000},
    {"name": "Shadow Ford", "performance": 30, "budget": 400000},
    {"name": "Surtees Ford", "performance": 30, "budget": 300000},
    {"name": "Iso Marlboro Ford", "performance": 25, "budget": 200000},
    {"name": "Tecno", "performance": 25, "budget": 100000},
]

teams_1974 = [
    {"name": "McLaren Ford", "performance": 75, "budget": 1000000},
    {"name": "Ferrari", "performance": 70, "budget": 900000},
    {"name": "Tyrrell Ford", "performance": 60, "budget": 800000},
    {"name": "Lotus Ford", "performance": 50, "budget": 700000},
    {"name": "Brabham Ford", "performance": 45, "budget": 600000},
    {"name": "Hesketh Ford", "performance": 30, "budget": 500000},
    {"name": "BRM", "performance": 25, "budget": 400000},
    {"name": "Shadow Ford", "performance": 20, "budget": 300000},
    {"name": "March Ford", "performance": 20, "budget": 200000},
    {"name": "Iso Marlboro Ford", "performance": 15, "budget": 100000},
    {"name": "Surtees Ford", "performance": 15, "budget": 100000},
    {"name": "Lola Ford", "performance": 10, "budget": 100000},
]

teams_1975 = [
    {"name": "Ferrari", "performance": 75, "budget": 1000000},
    {"name": "Brabham Ford", "performance": 65, "budget": 900000},
    {"name": "McLaren Ford", "performance": 65, "budget": 800000},
    {"name": "Hesketh Ford", "performance": 55, "budget": 700000},
    {"name": "Tyrrell Ford", "performance": 50, "budget": 600000},
    {"name": "Shadow Ford", "performance": 35, "budget": 500000},
    {"name": "Lotus Ford", "performance": 35, "budget": 400000},
    {"name": "March Ford", "performance": 30, "budget": 300000},
    {"name": "Frank Williams Racing Cars/Williams", "performance": 30, "budget": 200000},
    {"name": "Parnelli Ford", "performance": 30, "budget": 100000},
    {"name": "Hill Ford", "performance": 20, "budget": 100000},
    {"name": "Penske Ford", "performance": 20, "budget": 100000},
    {"name": "Ensign Ford", "performance": 20, "budget": 100000},
]

teams_1976 = [
    {"name": "Ferrari", "performance": 75, "budget": 1000000},
    {"name": "McLaren Ford", "performance": 70, "budget": 900000},
    {"name": "Tyrrell Ford", "performance": 70, "budget": 800000},
    {"name": "Lotus Ford", "performance": 50, "budget": 700000},
    {"name": "Penske Ford", "performance": 45, "budget": 600000},
    {"name": "Ligier Matra", "performance": 45, "budget": 600000},
    {"name": "Shadow Ford", "performance": 45, "budget": 500000},
    {"name": "Brabham Alfa Romeo", "performance": 45, "budget": 400000},
    {"name": "Surtees Ford", "performance": 40, "budget": 300000},
    {"name": "Fittipaldi Ford", "performance": 30, "budget": 200000},
    {"name": "Ensign Ford", "performance": 30, "budget": 100000},
    {"name": "Parnelli Ford", "performance": 30, "budget": 100000},
]

teams_1977 = [
    {"name": "Ferrari", "performance": 75, "budget": 1000000},
    {"name": "Lotus Ford", "performance": 65, "budget": 900000},
    {"name": "McLaren Ford", "performance": 65, "budget": 800000},
    {"name": "Wolf Ford", "performance": 60, "budget": 700000},
    {"name": "Brabham Alfa Romeo", "performance": 45, "budget": 600000},
    {"name": "Tyrrell Ford", "performance": 45, "budget": 600000},
    {"name": "Shadow Ford", "performance": 40, "budget": 500000},
    {"name": "Ligier Matra", "performance": 35, "budget": 400000},
    {"name": "Fittipaldi Ford", "performance": 30, "budget": 300000},
    {"name": "Ensign Ford", "performance": 30, "budget": 200000},
    {"name": "Surtees Ford", "performance": 25, "budget": 100000},
    {"name": "Penske Ford", "performance": 20, "budget": 100000},
]

teams_1978 = [
    {"name": "Lotus Ford", "performance": 75, "budget": 1000000},
    {"name": "Ferrari", "performance": 65, "budget": 900000},
    {"name": "Brabham Alfa Romeo", "performance": 65, "budget": 800000},
    {"name": "Tyrrell Ford", "performance": 55, "budget": 700000},
    {"name": "Wolf Ford", "performance": 45, "budget": 600000},
    {"name": "Ligier Matra", "performance": 40, "budget": 500000},
    {"name": "Fittipaldi Ford", "performance": 40, "budget": 400000},
    {"name": "McLaren Ford", "performance": 40, "budget": 300000},
    {"name": "Williams Ford", "performance": 35, "budget": 200000},
    {"name": "Arrows Ford", "performance": 35, "budget": 200000},
    {"name": "Shadow Ford", "performance": 30, "budget": 100000},
    {"name": "Renault", "performance": 25, "budget": 100000},
    {"name": "Surtees Ford", "performance": 20, "budget": 100000},
    {"name": "Ensign Ford", "performance": 20, "budget": 100000},
]

teams_1979 = [
    {"name": "Ferrari", "performance": 75, "budget": 1000000},
    {"name": "Williams Ford", "performance": 65, "budget": 900000},
    {"name": "Ligier Ford", "performance": 55, "budget": 800000},
    {"name": "Lotus Ford", "performance": 45, "budget": 700000},
    {"name": "Tyrrell Ford", "performance": 35, "budget": 600000},
    {"name": "Renault", "performance": 35, "budget": 500000},
    {"name": "McLaren Ford", "performance": 30, "budget": 400000},
    {"name": "Brabham Ford", "performance": 25, "budget": 300000},
    {"name": "Arrows Ford", "performance": 25, "budget": 200000},
    {"name": "Shadow Ford", "performance": 25, "budget": 100000},
    {"name": "ATS Ford", "performance": 25, "budget": 100000},
    {"name": "Fittipaldi Ford", "performance": 25, "budget": 100000},
]

teams_1980 = [
    {"name": "Williams Ford", "performance": 75, "budget": 1000000},
    {"name": "Ligier Ford", "performance": 60, "budget": 900000},
    {"name": "Brabham Ford", "performance": 60, "budget": 800000},
    {"name": "Renault", "performance": 50, "budget": 700000},
    {"name": "Lotus Ford", "performance": 35, "budget": 600000},
    {"name": "Tyrrell Ford", "performance": 35, "budget": 500000},
    {"name": "Arrows Ford", "performance": 35, "budget": 400000},
    {"name": "Fittipaldi Ford", "performance": 35, "budget": 400000},
    {"name": "McLaren Ford", "performance": 35, "budget": 400000},
    {"name": "Ferrari", "performance": 30, "budget": 300000},
    {"name": "Alfa Romeo", "performance": 25, "budget": 200000},
]

teams_1981 = [
    {"name": "Williams Ford", "performance": 75, "budget": 1000000},
    {"name": "Brabham Ford", "performance": 65, "budget": 900000},
    {"name": "Renault", "performance": 60, "budget": 800000},
    {"name": "Ligier Matra", "performance": 55, "budget": 700000},
    {"name": "Ferrari", "performance": 50, "budget": 600000},
    {"name": "McLaren Ford", "performance": 45, "budget": 500000},
    {"name": "Lotus Ford", "performance": 40, "budget": 400000},
    {"name": "Arrows Ford", "performance": 30, "budget": 300000},
    {"name": "Alfa Romeo", "performance": 30, "budget": 300000},
    {"name": "Tyrrell Ford", "performance": 30, "budget": 300000},
    {"name": "Ensign Ford", "performance": 25, "budget": 200000},
    {"name": "Theodore Ford", "performance": 20, "budget": 100000},
    {"name": "ATS Ford", "performance": 20, "budget": 100000},
]

teams_1982 = [
    {"name": "Ferrari", "performance": 75, "budget": 1000000},
    {"name": "McLaren Ford", "performance": 75, "budget": 900000},
    {"name": "Renault", "performance": 70, "budget": 800000},
    {"name": "Williams Ford", "performance": 70, "budget": 700000},
    {"name": "Lotus Ford", "performance": 60, "budget": 600000},
    {"name": "Tyrrell Ford", "performance": 55, "budget": 500000},
    {"name": "Brabham BMW", "performance": 55, "budget": 400000},
    {"name": "Ligier Matra", "performance": 55, "budget": 300000},
    {"name": "Brabham Ford", "performance": 55, "budget": 200000},
    {"name": "Alfa Romeo", "performance": 45, "budget": 100000},
    {"name": "Arrows Ford", "performance": 40, "budget": 100000},
    {"name": "ATS Ford", "performance": 40, "budget": 100000},
    {"name": "Osella Ford", "performance": 40, "budget": 100000},
    {"name": "Fittipaldi Ford", "performance": 35, "budget": 100000},
]

teams_1983 = [
    {"name": "Ferrari", "performance": 75, "budget": 1000000},
    {"name": "Renault", "performance": 70, "budget": 900000},
    {"name": "Brabham BMW", "performance": 70, "budget": 800000},
    {"name": "Williams Ford", "performance": 55, "budget": 700000},
    {"name": "McLaren Ford", "performance": 55, "budget": 600000},
    {"name": "Alfa Romeo", "performance": 45, "budget": 500000},
    {"name": "Tyrrell Ford", "performance": 40, "budget": 400000},
    {"name": "Lotus Renault", "performance": 40, "budget": 300000},
    {"name": "Toleman Hart", "performance": 40, "budget": 200000},
    {"name": "Arrows Ford", "performance": 30, "budget": 100000},
    {"name": "Williams Honda", "performance": 25, "budget": 100000},
    {"name": "Theodore Ford", "performance": 25, "budget": 100000},
    {"name": "Lotus Ford", "performance": 25, "budget": 100000},
]

teams_1984 = [
    {"name": "McLaren TAG", "performance": 80, "budget": 1000000},
    {"name": "Ferrari", "performance": 65, "budget": 900000},
    {"name": "Lotus Renault", "performance": 60, "budget": 800000},
    {"name": "Brabham BMW", "performance": 55, "budget": 700000},
    {"name": "Renault", "performance": 55, "budget": 600000},
    {"name": "Williams Honda", "performance": 50, "budget": 500000},
    {"name": "Toleman Hart", "performance": 40, "budget": 400000},
    {"name": "Alfa Romeo", "performance": 30, "budget": 300000},
    {"name": "Arrows BMW", "performance": 20, "budget": 200000},
    {"name": "Ligier Renault", "performance": 20, "budget": 200000},
    {"name": "Arrows Ford", "performance": 20, "budget": 200000},
    {"name": "Osella Alfa Romeo", "performance": 20, "budget": 100000},
]

teams_1985 = [
    {"name": "McLaren TAG", "performance": 80, "budget": 1000000},
    {"name": "Ferrari", "performance": 75, "budget": 900000},
    {"name": "Lotus Renault", "performance": 70, "budget": 800000},
    {"name": "Williams Honda", "performance": 70, "budget": 800000},
    {"name": "Brabham BMW", "performance": 55, "budget": 700000},
    {"name": "Ligier Renault", "performance": 55, "budget": 600000},
    {"name": "Renault", "performance": 50, "budget": 500000},
    {"name": "Arrows BMW", "performance": 50, "budget": 400000},
    {"name": "Tyrrell Ford", "performance": 40, "budget": 300000},
    {"name": "Tyrrell Renault", "performance": 40, "budget": 200000},
]

teams_1986 = [
    {"name": "Williams Honda", "performance": 90, "budget": 1000000},
    {"name": "McLaren TAG", "performance": 75, "budget": 900000},
    {"name": "Lotus Renault", "performance": 65, "budget": 800000},
    {"name": "Ferrari", "performance": 50, "budget": 700000},
    {"name": "Ligier Renault", "performance": 45, "budget": 600000},
    {"name": "Benetton BMW", "performance": 35, "budget": 500000},
    {"name": "Tyrrell Renault", "performance": 30, "budget": 400000},
    {"name": "Lola Ford", "performance": 25, "budget": 300000},
    {"name": "Brabham BMW", "performance": 20, "budget": 200000},
    {"name": "Arrows BMW", "performance": 20, "budget": 100000},
]

teams_1987 = [
    {"name": "Williams Honda", "performance": 90, "budget": 1000000},
    {"name": "McLaren TAG", "performance": 75, "budget": 900000},
    {"name": "Lotus Honda", "performance": 70, "budget": 800000},
    {"name": "Ferrari", "performance": 60, "budget": 700000},
    {"name": "Benetton Ford", "performance": 45, "budget": 600000},
    {"name": "Tyrrell Ford", "performance": 30, "budget": 500000},
    {"name": "Arrows Megatron", "performance": 30, "budget": 500000},
    {"name": "Brabham BMW", "performance": 30, "budget": 400000},
    {"name": "Lola Ford", "performance": 20, "budget": 300000},
    {"name": "Zakspeed", "performance": 20, "budget": 200000},
    {"name": "March Ford", "performance": 20, "budget": 100000},
    {"name": "Ligier Megatron", "performance": 20, "budget": 100000},
    {"name": "AGS Ford", "performance": 20, "budget": 100000},
]

teams_1988 = [
    {"name": "McLaren Honda", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 75, "budget": 900000},
    {"name": "Benetton Ford", "performance": 60, "budget": 800000},
    {"name": "Arrows Megatron", "performance": 50, "budget": 700000},
    {"name": "Lotus Honda", "performance": 50, "budget": 700000},
    {"name": "March Judd", "performance": 50, "budget": 600000},
    {"name": "Williams Judd", "performance": 50, "budget": 500000},
    {"name": "Tyrrell Ford", "performance": 35, "budget": 400000},
    {"name": "Rial Ford", "performance": 35, "budget": 300000},
    {"name": "Minardi Ford", "performance": 35, "budget": 200000},
]

teams_1989 = [
    {"name": "McLaren Honda", "performance": 90, "budget": 1000000},
    {"name": "Williams Renault", "performance": 75, "budget": 900000},
    {"name": "Ferrari", "performance": 65, "budget": 800000},
    {"name": "Benetton Ford", "performance": 55, "budget": 700000},
    {"name": "Tyrrell Ford", "performance": 40, "budget": 600000},
    {"name": "Lotus Judd", "performance": 40, "budget": 500000},
    {"name": "Arrows Ford", "performance": 40, "budget": 400000},
    {"name": "Dallara Ford", "performance": 35, "budget": 300000},
    {"name": "Brabham Judd", "performance": 35, "budget": 300000},
    {"name": "Onyx Ford", "performance": 35, "budget": 200000},
    {"name": "Minardi Judd", "performance": 35, "budget": 200000},
    {"name": "March Judd", "performance": 30, "budget": 100000},
    {"name": "Rial Ford", "performance": 30, "budget": 100000},
    {"name": "Ligier Ford", "performance": 30, "budget": 100000},
    {"name": "AGS Ford", "performance": 30, "budget": 100000},
    {"name": "Lola Lamborghini", "performance": 30, "budget": 100000},
]

teams_1990 = [
    {"name": "McLaren Honda", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "Benetton Ford", "performance": 70, "budget": 800000},
    {"name": "Williams Renault", "performance": 60, "budget": 700000},
    {"name": "Tyrrell Ford", "performance": 45, "budget": 600000},
    {"name": "Lola Lamborghini", "performance": 40, "budget": 500000},
    {"name": "Leyton House Judd", "performance": 35, "budget": 400000},
    {"name": "Lotus Lamborghini", "performance": 30, "budget": 300000},
    {"name": "Arrows Ford", "performance": 25, "budget": 200000},
    {"name": "Brabham Judd", "performance": 25, "budget": 200000},
]

teams_1991 = [
    {"name": "McLaren Honda", "performance": 90, "budget": 1000000},
    {"name": "Williams Renault", "performance": 85, "budget": 900000},
    {"name": "Ferrari", "performance": 70, "budget": 800000},
    {"name": "Benetton Ford", "performance": 60, "budget": 700000},
    {"name": "Jordan Ford", "performance": 45, "budget": 600000},
    {"name": "Tyrrell Honda", "performance": 45, "budget": 500000},
    {"name": "Minardi Ferrari", "performance": 35, "budget": 400000},
    {"name": "Dallara Judd", "performance": 35, "budget": 300000},
    {"name": "Lotus Judd", "performance": 30, "budget": 200000},
    {"name": "Brabham Yamaha", "performance": 30, "budget": 200000},
    {"name": "Lola Ford", "performance": 30, "budget": 100000},
    {"name": "Leyton House Ilmor", "performance": 30, "budget": 100000},
]

teams_1992 = [
    {"name": "Williams Renault", "performance": 90, "budget": 1000000},
    {"name": "McLaren Honda", "performance": 80, "budget": 900000},
    {"name": "Benetton Ford", "performance": 80, "budget": 800000},
    {"name": "Ferrari", "performance": 65, "budget": 700000},
    {"name": "Lotus Ford", "performance": 55, "budget": 600000},
    {"name": "Tyrrell Ilmor", "performance": 45, "budget": 500000},
    {"name": "Footwork Mugen Honda", "performance": 40, "budget": 400000},
    {"name": "Ligier Renault", "performance": 40, "budget": 400000},
    {"name": "March Ilmor", "performance": 35, "budget": 300000},
    {"name": "Dallara Ferrari", "performance": 35, "budget": 200000},
    {"name": "Jordan Yamaha", "performance": 30, "budget": 100000},
    {"name": "Minardi Lamborghini", "performance": 30, "budget": 100000},
    {"name": "Venturi Lamborghini", "performance": 30, "budget": 100000},
]

teams_1993 = [
    {"name": "Williams Renault", "performance": 90, "budget": 1000000},
    {"name": "McLaren Ford", "performance": 75, "budget": 900000},
    {"name": "Benetton Ford", "performance": 70, "budget": 800000},
    {"name": "Ferrari", "performance": 55, "budget": 700000},
    {"name": "Ligier Renault", "performance": 50, "budget": 600000},
    {"name": "Lotus Ford", "performance": 40, "budget": 500000},
    {"name": "Sauber", "performance": 40, "budget": 500000},
    {"name": "Minardi Ford", "performance": 35, "budget": 400000},
    {"name": "Footwork Mugen Honda", "performance": 30, "budget": 300000},
    {"name": "Larrousse Lamborghini", "performance": 30, "budget": 200000},
    {"name": "Jordan Hart", "performance": 30, "budget": 200000},
]

teams_1994 = [
    {"name": "Williams Renault", "performance": 90, "budget": 1000000},
    {"name": "Benetton Ford", "performance": 85, "budget": 900000},
    {"name": "Ferrari", "performance": 75, "budget": 800000},
    {"name": "McLaren Peugeot", "performance": 65, "budget": 700000},
    {"name": "Jordan Hart", "performance": 55, "budget": 600000},
    {"name": "Ligier Renault", "performance": 45, "budget": 500000},
    {"name": "Tyrrell Yamaha", "performance": 45, "budget": 500000},
    {"name": "Sauber Mercedes", "performance": 45, "budget": 400000},
    {"name": "Footwork Ford", "performance": 40, "budget": 300000},
    {"name": "Minardi Ford", "performance": 35, "budget": 200000},
    {"name": "Larrousse Ford", "performance": 30, "budget": 100000},
]

teams_1995 = [
    {"name": "Benetton Renault", "performance": 90, "budget": 1000000},
    {"name": "Williams Renault", "performance": 85, "budget": 900000},
    {"name": "Ferrari", "performance": 75, "budget": 800000},
    {"name": "McLaren Mercedes", "performance": 60, "budget": 700000},
    {"name": "Ligier Mugen Honda", "performance": 55, "budget": 600000},
    {"name": "Jordan Peugeot", "performance": 50, "budget": 500000},
    {"name": "Sauber Ford", "performance": 45, "budget": 400000},
    {"name": "Footwork Hart", "performance": 35, "budget": 300000},
    {"name": "Tyrrell Yamaha", "performance": 35, "budget": 300000},
    {"name": "Minardi Ford", "performance": 30, "budget": 200000},
]

teams_1996 = [
    {"name": "Williams Renault", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 80, "budget": 900000},
    {"name": "Benetton Renault", "performance": 80, "budget": 800000},
    {"name": "McLaren Mercedes", "performance": 70, "budget": 700000},
    {"name": "Jordan Peugeot", "performance": 60, "budget": 600000},
    {"name": "Ligier Mugen Honda", "performance": 55, "budget": 500000},
    {"name": "Sauber Ford", "performance": 50, "budget": 400000},
    {"name": "Tyrrell Yamaha", "performance": 40, "budget": 300000},
    {"name": "Footwork Hart", "performance": 40, "budget": 300000},
]

teams_1997 = [
    {"name": "Williams Renault", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "Benetton Renault", "performance": 75, "budget": 800000},
    {"name": "McLaren Mercedes", "performance": 75, "budget": 700000},
    {"name": "Jordan Peugeot", "performance": 60, "budget": 600000},
    {"name": "Prost Mugen Honda", "performance": 50, "budget": 500000},
    {"name": "Sauber Petronas", "performance": 45, "budget": 400000},
    {"name": "Arrows Yamaha", "performance": 40, "budget": 300000},
    {"name": "Stewart Ford", "performance": 35, "budget": 200000},
    {"name": "Tyrrell Ford", "performance": 30, "budget": 100000},
]

teams_1998 = [
    {"name": "McLaren Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "Williams Mecachrome", "performance": 70, "budget": 800000},
    {"name": "Jordan Mugen Honda", "performance": 65, "budget": 700000},
    {"name": "Benetton Playlife", "performance": 65, "budget": 600000},
    {"name": "Sauber Petronas", "performance": 55, "budget": 500000},
    {"name": "Arrows", "performance": 50, "budget": 400000},
    {"name": "Stewart Ford", "performance": 50, "budget": 300000},
    {"name": "Prost Peugeot", "performance": 45, "budget": 200000},
]

teams_1999 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 90, "budget": 900000},
    {"name": "Jordan Mugen Honda", "performance": 75, "budget": 800000},
    {"name": "Stewart Ford", "performance": 60, "budget": 700000},
    {"name": "Williams Supertec", "performance": 60, "budget": 600000},
    {"name": "Benetton Playlife", "performance": 50, "budget": 500000},
    {"name": "Prost Peugeot", "performance": 40, "budget": 400000},
    {"name": "Sauber Petronas", "performance": 30, "budget": 300000},
    {"name": "Minardi Ford", "performance": 25, "budget": 200000},
    {"name": "Arrows", "performance": 25, "budget": 200000},
]

teams_2000 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 900000},
    {"name": "Williams BMW", "performance": 70, "budget": 800000},
    {"name": "Benetton Playlife", "performance": 65, "budget": 700000},
    {"name": "BAR Honda", "performance": 65, "budget": 700000},
    {"name": "Jordan Mugen Honda", "performance": 60, "budget": 600000},
    {"name": "Arrows Supertec", "performance": 50, "budget": 500000},
    {"name": "Sauber Petronas", "performance": 50, "budget": 400000},
    {"name": "Jaguar Cosworth", "performance": 45, "budget": 300000},
]

teams_2001 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 80, "budget": 900000},
    {"name": "Williams BMW", "performance": 70, "budget": 800000},
    {"name": "Sauber Petronas", "performance": 55, "budget": 700000},
    {"name": "Jordan Honda", "performance": 55, "budget": 600000},
    {"name": "BAR Honda", "performance": 50, "budget": 500000},
    {"name": "Benetton Renault", "performance": 40, "budget": 400000},
    {"name": "Jaguar Cosworth", "performance": 40, "budget": 300000},
    {"name": "Prost Acer", "performance": 35, "budget": 200000},
    {"name": "Arrows Asiatech", "performance": 30, "budget": 100000},
]

teams_2002 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "Williams BMW", "performance": 75, "budget": 900000},
    {"name": "McLaren Mercedes", "performance": 65, "budget": 800000},
    {"name": "Renault", "performance": 55, "budget": 700000},
    {"name": "Sauber Petronas", "performance": 45, "budget": 600000},
    {"name": "Jordan Honda", "performance": 35, "budget": 500000},
    {"name": "Jaguar Cosworth", "performance": 35, "budget": 400000},
    {"name": "BAR Honda", "performance": 35, "budget": 300000},
    {"name": "Minardi Asiatech", "performance": 30, "budget": 200000},
    {"name": "Toyota", "performance": 30, "budget": 200000},
    {"name": "Arrows Cosworth", "performance": 30, "budget": 200000},
]

teams_2003 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "Williams BMW", "performance": 85, "budget": 900000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 800000},
    {"name": "Renault", "performance": 75, "budget": 700000},
    {"name": "BAR Honda", "performance": 65, "budget": 600000},
    {"name": "Sauber Petronas", "performance": 60, "budget": 500000},
    {"name": "Jaguar Cosworth", "performance": 60, "budget": 400000},
    {"name": "Toyota", "performance": 55, "budget": 300000},
    {"name": "Jordan Ford", "performance": 50, "budget": 200000},
    {"name": "Minardi Cosworth", "performance": 40, "budget": 100000},
]

teams_2004 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "BAR Honda", "performance": 80, "budget": 900000},
    {"name": "Renault", "performance": 75, "budget": 800000},
    {"name": "Williams BMW", "performance": 70, "budget": 700000},
    {"name": "McLaren Mercedes", "performance": 60, "budget": 600000},
    {"name": "Sauber Petronas", "performance": 50, "budget": 500000},
    {"name": "Jaguar Cosworth", "performance": 40, "budget": 400000},
    {"name": "Toyota", "performance": 40, "budget": 300000},
    {"name": "Jordan Ford", "performance": 35, "budget": 200000},
    {"name": "Minardi Cosworth", "performance": 30, "budget": 100000},
]

teams_2005 = [
    {"name": "Renault", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 900000},
    {"name": "Ferrari", "performance": 75, "budget": 800000},
    {"name": "Toyota", "performance": 70, "budget": 700000},
    {"name": "Williams BMW", "performance": 60, "budget": 600000},
    {"name": "BAR Honda", "performance": 50, "budget": 500000},
    {"name": "RBR Cosworth", "performance": 45, "budget": 400000},
    {"name": "Sauber Petronas", "performance": 35, "budget": 300000},
    {"name": "Jordan Toyota", "performance": 25, "budget": 200000},
    {"name": "Minardi Cosworth", "performance": 20, "budget": 100000},
]

teams_2006 = [
    {"name": "Renault", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 90, "budget": 900000},
    {"name": "McLaren Mercedes", "performance": 75, "budget": 800000},
    {"name": "Honda", "performance": 70, "budget": 700000},
    {"name": "Sauber BMW", "performance": 60, "budget": 600000},
    {"name": "Toyota", "performance": 60, "budget": 500000},
    {"name": "RBR Ferrari", "performance": 50, "budget": 400000},
    {"name": "Williams Cosworth", "performance": 45, "budget": 300000},
    {"name": "STR Cosworth", "performance": 35, "budget": 200000},
    {"name": "MF1 Toyota", "performance": 25, "budget": 100000},
    {"name": "Super Aguri Honda", "performance": 25, "budget": 100000},
]

teams_2007 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "Sauber BMW", "performance": 80, "budget": 900000},
    {"name": "Renault", "performance": 70, "budget": 800000},
    {"name": "Williams Toyota", "performance": 60, "budget": 700000},
    {"name": "Red Bull Renault", "performance": 50, "budget": 600000},
    {"name": "Toyota", "performance": 40, "budget": 500000},
    {"name": "STR Ferrari", "performance": 30, "budget": 400000},
    {"name": "Honda", "performance": 25, "budget": 300000},
    {"name": "Super Aguri Honda", "performance": 20, "budget": 200000},
    {"name": "Spyker Ferrari", "performance": 15, "budget": 100000},
    {"name": "McLaren Mercedes", "performance": 90, "budget": 100000},
]

teams_2008 = [
    {"name": "Ferrari", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 900000},
    {"name": "Sauber BMW", "performance": 80, "budget": 800000},
    {"name": "Renault", "performance": 70, "budget": 700000},
    {"name": "Toyota", "performance": 60, "budget": 600000},
    {"name": "STR Ferrari", "performance": 55, "budget": 500000},
    {"name": "Red Bull Renault", "performance": 45, "budget": 400000},
    {"name": "Williams Toyota", "performance": 40, "budget": 300000},
    {"name": "Honda", "performance": 35, "budget": 200000},
    {"name": "Force India Ferrari", "performance": 20, "budget": 100000},
    {"name": "Super Aguri Honda", "performance": 20, "budget": 100000},
]

teams_2009 = [
    {"name": "Brawn Mercedes", "performance": 90, "budget": 1000000},
    {"name": "RBR Renault", "performance": 85, "budget": 900000},
    {"name": "McLaren Mercedes", "performance": 75, "budget": 800000},
    {"name": "Ferrari", "performance": 75, "budget": 700000},
    {"name": "Toyota", "performance": 70, "budget": 600000},
    {"name": "Sauber BMW", "performance": 60, "budget": 500000},
    {"name": "Williams Toyota", "performance": 60, "budget": 400000},
    {"name": "Renault", "performance": 55, "budget": 300000},
    {"name": "Force India Mercedes", "performance": 45, "budget": 200000},
    {"name": "STR Ferrari", "performance": 35, "budget": 100000},
]

teams_2010 = [
    {"name": "RBR Renault", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 900000},
    {"name": "Ferrari", "performance": 80, "budget": 800000},
    {"name": "Mercedes", "performance": 70, "budget": 700000},
    {"name": "Renault", "performance": 65, "budget": 600000},
    {"name": "Williams Cosworth", "performance": 55, "budget": 500000},
    {"name": "Force India Mercedes", "performance": 55, "budget": 400000},
    {"name": "Sauber Ferrari", "performance": 45, "budget": 300000},
    {"name": "STR Ferrari", "performance": 35, "budget": 200000},
    {"name": "Lotus Cosworth", "performance": 25, "budget": 100000},
    {"name": "HRT Cosworth", "performance": 25, "budget": 100000},
    {"name": "Virgin Cosworth", "performance": 25, "budget": 100000},
]

teams_2011 = [
    {"name": "Red Bull Racing Renault", "performance": 90, "budget": 1000000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 900000},
    {"name": "Ferrari", "performance": 75, "budget": 800000},
    {"name": "Mercedes", "performance": 65, "budget": 700000},
    {"name": "Renault", "performance": 55, "budget": 600000},
    {"name": "Force India Mercedes", "performance": 50, "budget": 500000},
    {"name": "Sauber Ferrari", "performance": 45, "budget": 400000},
    {"name": "STR Ferrari", "performance": 45, "budget": 300000},
    {"name": "Williams Cosworth", "performance": 40, "budget": 200000},
    {"name": "Lotus Renault", "performance": 35, "budget": 100000},
    {"name": "HRT Renault", "performance": 35, "budget": 100000},
    {"name": "Virgin Renault", "performance": 35, "budget": 100000},
]

teams_2012 = [
    {"name": "Red Bull Racing Renault", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "McLaren Mercedes", "performance": 85, "budget": 800000},
    {"name": "Lotus Renault", "performance": 80, "budget": 700000},
    {"name": "Mercedes", "performance": 70, "budget": 600000},
    {"name": "Sauber Ferrari", "performance": 65, "budget": 500000},
    {"name": "Force India Mercedes", "performance": 60, "budget": 400000},
    {"name": "Williams Renault", "performance": 55, "budget": 300000},
    {"name": "STR Ferrari", "performance": 45, "budget": 200000},
    {"name": "Caterham Renault", "performance": 35, "budget": 100000},
    {"name": "Marussia Cosworth", "performance": 35, "budget": 100000},
    {"name": "HRT Cosworth", "performance": 35, "budget": 100000},
]

teams_2013 = [
    {"name": "Red Bull Racing Renault", "performance": 90, "budget": 1000000},
    {"name": "Mercedes", "performance": 80, "budget": 900000},
    {"name": "Ferrari", "performance": 80, "budget": 800000},
    {"name": "Lotus Renault", "performance": 80, "budget": 700000},
    {"name": "McLaren Mercedes", "performance": 70, "budget": 600000},
    {"name": "Force India Mercedes", "performance": 65, "budget": 500000},
    {"name": "Sauber Ferrari", "performance": 60, "budget": 400000},
    {"name": "STR Ferrari", "performance": 55, "budget": 300000},
    {"name": "Williams Renault", "performance": 45, "budget": 200000},
    {"name": "Marussia Cosworth", "performance": 35, "budget": 100000},
    {"name": "Caterham Renault", "performance": 35, "budget": 100000},
]

teams_2014 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Red Bull Racing Renault", "performance": 80, "budget": 900000},
    {"name": "Williams Mercedes", "performance": 75, "budget": 800000},
    {"name": "Ferrari", "performance": 65, "budget": 700000},
    {"name": "McLaren Mercedes", "performance": 60, "budget": 600000},
    {"name": "Force India Mercedes", "performance": 55, "budget": 500000},
    {"name": "STR Renault", "performance": 45, "budget": 400000},
    {"name": "Lotus Renault", "performance": 35, "budget": 300000},
    {"name": "Marussia Ferrari", "performance": 25, "budget": 200000},
    {"name": "Sauber Ferrari", "performance": 20, "budget": 100000},
    {"name": "Caterham Renault", "performance": 20, "budget": 100000},
]

teams_2015 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 80, "budget": 900000},
    {"name": "Williams Mercedes", "performance": 70, "budget": 800000},
    {"name": "Red Bull Racing Renault", "performance": 65, "budget": 700000},
    {"name": "Force India Mercedes", "performance": 60, "budget": 600000},
    {"name": "Lotus Mercedes", "performance": 50, "budget": 500000},
    {"name": "STR Renault", "performance": 45, "budget": 400000},
    {"name": "Sauber Ferrari", "performance": 40, "budget": 300000},
    {"name": "McLaren Honda", "performance": 35, "budget": 200000},
    {"name": "Marussia Ferrari", "performance": 25, "budget": 100000},
]

teams_2016 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Red Bull Racing TAG Heuer", "performance": 80, "budget": 900000},
    {"name": "Ferrari", "performance": 75, "budget": 800000},
    {"name": "Force India Mercedes", "performance": 65, "budget": 700000},
    {"name": "Williams Mercedes", "performance": 60, "budget": 600000},
    {"name": "McLaren Honda", "performance": 55, "budget": 500000},
    {"name": "Toro Rosso Ferrari", "performance": 50, "budget": 400000},
    {"name": "Haas Ferrari", "performance": 40, "budget": 300000},
    {"name": "Renault", "performance": 30, "budget": 200000},
    {"name": "Sauber Ferrari", "performance": 25, "budget": 100000},
    {"name": "MRT Mercedes", "performance": 25, "budget": 100000},
]

teams_2017 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "Red Bull Racing TAG Heuer", "performance": 75, "budget": 800000},
    {"name": "Force India Mercedes", "performance": 65, "budget": 700000},
    {"name": "Williams Mercedes", "performance": 55, "budget": 600000},
    {"name": "Renault", "performance": 50, "budget": 500000},
    {"name": "Toro Rosso", "performance": 50, "budget": 400000},
    {"name": "Haas Ferrari", "performance": 45, "budget": 300000},
    {"name": "McLaren Honda", "performance": 40, "budget": 200000},
    {"name": "Sauber Ferrari", "performance": 30, "budget": 100000},
]

teams_2018 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "Red Bull Racing TAG Heuer", "performance": 80, "budget": 800000},
    {"name": "Renault", "performance": 70, "budget": 700000},
    {"name": "Haas Ferrari", "performance": 65, "budget": 600000},
    {"name": "McLaren Renault", "performance": 60, "budget": 500000},
    {"name": "Force India Mercedes", "performance": 55, "budget": 400000},
    {"name": "Sauber Ferrari", "performance": 50, "budget": 300000},
    {"name": "Scuderia Toro Rosso Honda", "performance": 45, "budget": 200000},
    {"name": "Williams Mercedes", "performance": 35, "budget": 100000},
]

teams_2019 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 80, "budget": 900000},
    {"name": "Red Bull Racing Honda", "performance": 75, "budget": 800000},
    {"name": "McLaren Renault", "performance": 65, "budget": 700000},
    {"name": "Renault", "performance": 60, "budget": 600000},
    {"name": "Scuderia Toro Rosso Honda", "performance": 60, "budget": 500000},
    {"name": "Racing Point BWT Mercedes", "performance": 55, "budget": 400000},
    {"name": "Alfa Romeo Racing Ferrari", "performance": 50, "budget": 300000},
    {"name": "Haas Ferrari", "performance": 40, "budget": 200000},
    {"name": "Williams Mercedes", "performance": 30, "budget": 100000},
]

teams_2020 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Red Bull Racing Honda", "performance": 80, "budget": 900000},
    {"name": "McLaren Renault", "performance": 70, "budget": 800000},
    {"name": "Racing Point BWT Mercedes", "performance": 70, "budget": 700000},
    {"name": "Renault", "performance": 70, "budget": 600000},
    {"name": "Ferrari", "performance": 65, "budget": 500000},
    {"name": "AlphaTauri Honda", "performance": 60, "budget": 400000},
    {"name": "Alfa Romeo Racing Ferrari", "performance": 50, "budget": 300000},
    {"name": "Haas Ferrari", "performance": 45, "budget": 200000},
    {"name": "Williams Mercedes", "performance": 40, "budget": 100000},
]

teams_2021 = [
    {"name": "Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Red Bull Racing Honda", "performance": 90, "budget": 900000},
    {"name": "Ferrari", "performance": 80, "budget": 800000},
    {"name": "McLaren Mercedes", "performance": 75, "budget": 700000},
    {"name": "Alpine Renault", "performance": 70, "budget": 600000},
    {"name": "AlphaTauri Honda", "performance": 70, "budget": 500000},
    {"name": "Aston Martin Mercedes", "performance": 60, "budget": 400000},
    {"name": "Williams Mercedes", "performance": 50, "budget": 300000},
    {"name": "Alfa Romeo Racing Ferrari", "performance": 50, "budget": 200000},
    {"name": "Haas Ferrari", "performance": 45, "budget": 100000},
]

teams_2022 = [
    {"name": "Red Bull Racing RBPT", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 85, "budget": 900000},
    {"name": "Mercedes", "performance": 85, "budget": 800000},
    {"name": "Alpine Renault", "performance": 75, "budget": 700000},
    {"name": "McLaren Mercedes", "performance": 75, "budget": 600000},
    {"name": "Alfa Romeo Ferrari", "performance": 65, "budget": 500000},
    {"name": "Aston Martin Mercedes", "performance": 65, "budget": 500000},
    {"name": "Haas Ferrari", "performance": 60, "budget": 400000},
    {"name": "AlphaTauri RBPT", "performance": 60, "budget": 300000},
    {"name": "Williams Mercedes", "performance": 50, "budget": 200000},
]

teams_2023 = [
    {"name": "Red Bull Racing Honda RBPT", "performance": 90, "budget": 1000000},
    {"name": "Mercedes", "performance": 80, "budget": 900000},
    {"name": "Ferrari", "performance": 80, "budget": 800000},
    {"name": "McLaren Mercedes", "performance": 75, "budget": 700000},
    {"name": "Aston Martin Aramco Mercedes", "performance": 75, "budget": 600000},
    {"name": "Alpine Renault", "performance": 65, "budget": 500000},
    {"name": "Williams Mercedes", "performance": 55, "budget": 400000},
    {"name": "AlphaTauri Honda RBPT", "performance": 55, "budget": 300000},
    {"name": "Alfa Romeo Ferrari", "performance": 55, "budget": 200000},
    {"name": "Haas Ferrari", "performance": 50, "budget": 100000},
]

teams_2024 = [
    {"name": "McLaren Mercedes", "performance": 90, "budget": 1000000},
    {"name": "Ferrari", "performance": 90, "budget": 900000},
    {"name": "Red Bull Racing Honda RBPT", "performance": 85, "budget": 800000},
    {"name": "Mercedes", "performance": 80, "budget": 700000},
    {"name": "Aston Martin Aramco Mercedes", "performance": 70, "budget": 600000},
    {"name": "Alpine Renault", "performance": 65, "budget": 500000},
    {"name": "Haas Ferrari", "performance": 65, "budget": 400000},
    {"name": "RB Honda RBPT", "performance": 65, "budget": 300000},
    {"name": "Williams Mercedes", "performance": 60, "budget": 200000},
    {"name": "Kick Sauber Ferrari", "performance": 55, "budget": 100000},
]

# Tracks Data
tracks_1950 = ["British GP (Silverstone Circuit)", "Monaco GP (Circuit de Monaco)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Swiss GP (Circuit Bremgarten)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "Italian GP (Autodromo Nazionale di Monza)"]
tracks_1951 = ["Swiss GP (Circuit Bremgarten)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "Spanish GP (Pedralbes Circuit)"]
tracks_1952 = ["Swiss GP (Circuit Bremgarten)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Rouen-Les-Essarts)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)"]
tracks_1953 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Dutch GP (Circuit Zandvoort)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Swiss GP (Circuit Bremgarten)", "Italian GP (Autodromo Nazionale di Monza)"]
tracks_1954 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Swiss GP (Circuit Bremgarten)", "Italian GP (Autodromo Nazionale di Monza)", "Spanish GP (Pedralbes Circuit)"]
tracks_1955 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Monaco GP (Circuit de Monaco)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "British GP (Aintree Motor Racing Circuit)", "Italian GP (Autodromo Nazionale di Monza)"]
tracks_1956 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Monaco GP (Circuit de Monaco)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)"]
tracks_1957 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Monaco GP (Circuit de Monaco)", "Indianapolis 500 (Indianapolis Motor Speedway)", "French GP (Rouen-Les-Essarts)", "British GP (Aintree Motor Racing Circuit)", "German GP (Nürburgring)", "Pescara GP (Pescara Circuit)", "Italian GP (Autodromo Nazionale di Monza)"]
tracks_1958 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Monaco GP (Circuit de Monaco)", "Dutch GP (Circuit Zandvoort)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Portugese GP (Circuito da Boavista)", "Italian GP (Autodromo Nazionale di Monza)", "Moroccan GP (Ain-Diab Circuit)"]
tracks_1959 = ["Monaco GP (Circuit de Monaco)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Dutch GP (Circuit Zandvoort)", "French GP (Reims-Gueux)", "British GP (Aintree Motor Racing Circuit)", "German GP (AVUS)", "Portugese GP (Monsanto Park Circuit)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Sebring International Raceway)"]
tracks_1960 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Monaco GP (Circuit de Monaco)", "Indianapolis 500 (Indianapolis Motor Speedway)", "Dutch GP (Circuit Zandvoort)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "Portugese GP (Circito da Boavista)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Riverside International Raceway)"]
tracks_1961 = ["Monaco GP (Circuit de Monaco)", "Dutch GP (Circuit Zandvoort)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Aintree Motor Racing Circuit)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)"]
tracks_1962 = ["Dutch GP (Circuit Zandvoort)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Rouen-Les-Essarts)", "British GP (Aintree Motor Racing Circuit)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)", "South African GP (Prince George Circuit)"]
tracks_1963 = ["Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "French GP (Reims-Gueux)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)", "South African GP (Prince George Circuit)"]
tracks_1964 = ["Monaco GP (Circuit de Monaco)", "Dutch GP (Circuit Park Zandvoort)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Rouen-Les-Essarts)", "British GP (Brands Hatch)", "German GP (Nürburgring)", "Austrian GP (Zeltweg Air Base)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1965 = ["South African GP (Prince George Circuit)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Charade Circuit)", "British GP (Silverstone Circuit)", "Dutch GP (Circuit Zandvoort)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1966 = ["Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Reims-Gueux)", "British GP (Brands Hatch)", "Dutch GP (Circuit Park Zandvoort)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1967 = ["South African GP (Kyalami Grand Prix Circuit)", "Monaco GP (Circuit de Monaco)", "Dutch GP (Circuit Zandvoort)", "Belgian GP (Circuit de Spa-Francorchamps)", "French GP (Bugatti Circuit)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Canadian GP (Mosport Park)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1968 = ["South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "French GP (Rouen-Les-Essarts)", "British GP (Brands Hatch)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Circuit Mont-Tremblant)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1969 = ["South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Montjuïc circuit)", "Monaco GP (Circuit de Monaco)", "Dutch GP (Circuit Zandvoort)", "French GP (Charade Circuit)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Mosport Park)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1970 = ["South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "French GP (Charade Circuit)", "British GP (Brands Hatch)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Circuit Monst-Tremblant)", "United States GP (Watkins Glen International)", "Mexican GP (Magdalena Mixhuca)"]
tracks_1971 = ["South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Montjuïc circuit)", "Monaco GP (Circuit de Monaco)", "Dutch GP (Circuit Zandvoort)", "French GP (Paul Ricard Circuit)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Mosport Park)", "United States GP (Watkins Glen International)"]
tracks_1972 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Nivelles-Baulers)", "French GP (Charade Circuit)", "British GP (Brands Hatch)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Mosport Park)", "United States GP (Watkins Glen International)"]
tracks_1973 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Montjuïc circuit)", "Belgian GP (Circuit Zolder)", "Monaco GP (Circuit de Monaco)", "Swedish GP (Scandinavian Raceway)", "French GP (Paul Ricard Circuit)", "British GP (Silverstone Circuit)", "Dutch GP (Circuit Zandvoort)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Mosport Park)", "United States GP (Watkins Glen International)"]
tracks_1974 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Belgian GP (Nivelles-Baulers)", "Monaco GP (Circuit de Monaco)", "Swedish GP (Scandinavian Raceway)", "Dutch GP (Circuit Zandvoort)", "French GP (Dijon-Prenois)", "British GP (Brands Hatch)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Mosport Park)", "United States GP (Watkins Glen International)"]
tracks_1975 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "Spanish GP (Montjuïc circuit)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit Zolder)", "Swedish GP (Scandinavian Raceway)", "Dutch GP (Circuit Zandvoort)", "French GP (Paul Ricard Circuit)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen Grand Prix Course)"]
tracks_1976 = ["Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "United States GP West (Long Beach Street Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Belgian GP (Circuit Zolder)", "Monaco GP (Circuit de Monaco)", "Swedish GP (Scandinavian Raceway)", "French GP (Circuit Paul Ricard)", "British GP (Brands Hatch)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Mosport Park)", "United States GP (Watkins Glen Grand Prix Course)", "Japanese GP (Fuji Speedway)"]
tracks_1977 = ["Argentine GP (Autodromo De Buenos Aires)", "Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "United States GP West (Long Beach Street Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit Zolder)", "Swedish GP (Scandinavian Raceway)", "French GP (Dijon-Prenois)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen Grand Prix Course)", "Canadian GP (Mosport Park)", "Japanese GP (Fuji Speedway)"]
tracks_1978 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Brazilian GP (Jacarepaguá)", "South African GP (Kyalami Grand Prix Circuit)", "United States GP West (Long Beach Street Circuit)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Zolder)", "Spanish GP (Circuito Permanente Del Jarama)", "Swedish GP (Scandinavian Raceway)", "French GP (Paul Ricard Circuit)", "British GP (Brands Hatch)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Watkins Glen Grand Prix Course)", "Canadian GP (Île Notre-Dame Circuit)"]
tracks_1979 = ["Argentine GP (Autódromo Oscar Alfredo Gálvez)", "Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "United States GP West (Long Beach Street Circuit)", "Spanish GP (Circuito Permanente Del Jarama)", "Belgian GP (Circuit Zolder)", "Monaco GP (Circuit de Monaco)", "French GP (Dijon-Prenois)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Île Notre-Dame Circuit)", "United States GP (Watkins Glen Grand Prix Course)"]
tracks_1980 = ["Argentine GP (Autódromo De Buenos Aires)", "Brazilian GP (Autodromo de Interlagos)", "South African GP (Kyalami Grand Prix Circuit)", "United States GP West (Long Beach Street Circuit)", "Belgian GP (Zolder)", "Monaco GP (Circuit de Monaco)", "French GP (Paul Ricard Circuit)", "British GP (Brands Hatch)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Dino Ferrari)", "Canadian GP (Île Notre-Dame Circuit)", "United States GP (Watkins Glen Grand Prix Course)"]
tracks_1981 = ["United States GP West (Long Beach Street Circuit)", "Brazilian GP (Autódromo de Jacarepaguá)", "Argentine GP (Autodromo De Buenos Aires)", "San Marino GP (Autodromo Dino Ferrari)", "Belgian GP (Circuit Zolder)", "Monaco GP (Circuit de Monaco)", "Spanish GP (Circuito Permanente Del Jarama)", "French GP (Dijon-Prenois)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "Canadian GP (Île Notre-Dame Circuit)", "Caesars Palace GP (Caesars Palace Grand Prix Circuit)"]
tracks_1982 = ["South African GP (Kyalami Grand Prix Circuit)", "Brazilian GP (Jacarepaguá)", "United States GP West (Long Beach Street Circuit)", "San Marino GP (Autodromo Dino Ferrari)", "Belgian GP (Circuit Zolder)", "Monaco GP (Circuit de Monaco)", "Detroit GP (Detroit Street Circuit)", "Canadian GP (Circuit Gilles Villeneuve)", "Dutch GP (Circuit Park Zandvoort)", "British GP (Brands Hatch)", "French GP (Circuit Paul Ricard)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Swiss GP (Dijon-Prenois)", "Italian GP (Autodromo Nazionale di Monza)", "Caesars Palace GP (Caesars Palace Grand Prix Circuit)"]
tracks_1983 = ["Brazilian GP (Jacarepaguá)", "United States GP West (Long Beach Street Circuit)", "French GP (Circuit Paul Ricard)", "San Marino GP (Autodromo Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "Detroit GP (Detroit Street Circuit)", "Canadian GP (Circuit Gilles Villeneuve)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Park Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "European GP (Brands Hatch)", "South African GP (Kyalami Grand Prix Circuit)"]
tracks_1984 = ["Brazilian GP (Jacarepaguá)", "South African GP (Kyalami Grand Prix Circuit)", "Belgian GP (Circuit Zolder)", "San Marino GP (Autodromo Dino Ferrari)", "French GP (Dijon-Prenois)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Detroit GP (Detroit Street Circuit)", "Dallas GP (Fair Park Street Circuit)", "British GP (Brands Hatch)", "German GP (Hockenheimring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Park Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "European GP (Nürburgring)", "Portuguese GP (Autodromo do Estoril)"]
tracks_1985 = ["Brazilian GP (Autodromo Jacarepaguá)", "Portuguese GP (Autodromo do Estoril)", "San Marino GP (Autodromo Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Detroit GP (Detroit Street Circuit)", "French GP (Paul Ricard Circuit)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Austrian GP (Österreichring)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Autodromo Nazionale di Monza)", "Belgian GP (Circuit de Spa-Francorchamps)", "European GP (Brands Hatch)", "South African GP (Kyalami Grand Prix Circuit)", "Australian GP (Adelaide Street Circuit)"]
tracks_1986 = ["Brazilian GP (Autodromo de Jacarepaguá)", "Spanish GP (Circuito de Jerez)", "San Marino GP (Autodromo Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Belgian GP (Circuit de Spa-Francorchamps)", "Canadian GP (Circuit Gilles Villeneuve)", "Detroit GP (Detroit Street Circuit)", "French GP (Paul Ricard Circuit)", "British GP (Brands Hatch)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autodromo do Estoril)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Australian GP (Adelaide Street Circuit)"]
tracks_1987 = ["Brazilian GP (Autodromo Jacarepaguá)", "San Marino GP (Autodromo Dino Ferrari)", "Belgian GP (Circuit de Spa-Francorchamps)", "Monaco GP (Circuit de Monaco)", "Detroit GP (Detroit Street Circuit)", "French GP (Paul Ricard Circuit)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Austrian GP (Österreichring)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autodromo do Estoril)", "Spanish GP (Circuito de Jerez)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Japanese GP (Suzuka International Racing Course)", "Australian GP (Adelaide Street Circuit)"]
tracks_1988 = ["Brazilian GP (Autódromo Internacional Nelson Piquet)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Canadian GP (Circuit Gilles Villeneuve)", "Detroit GP (Detroit Street Circuit)", "French GP (Circuit Paul Ricard)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Spanish GP (Circuito de Jerez)", "Japanese GP (Suzuka International Racing Course)", "Australian GP (Adelaide Street Circuit)"]
tracks_1989 = ["Brazilian GP (Autódromo Internacional Nelson Piquet)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Mexican GP (Autódromo Hermanos Rodríguez)", "United States GP (Phoenix Street Circuit)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit Paul Ricard)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Spanish GP (Circuito de Jerez)", "Japanese GP (Suzuka Circuit)", "Australian GP (Adelaide Street Circuit)"]
tracks_1990 = ["United States GP (Phoenix Street Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Mexican GP (Autódromo Hermanos Rodríguez)", "French GP (Circuit Paul Ricard)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Spanish GP (Circuito de Jerez)", "Japanese GP (Suzuka Circuit)", "Australian GP (Adelaide Street Circuit)"]
tracks_1991 = ["United States GP (Phoenix Street Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Mexican GP (Autódromo Hermanos Rodríguez)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Japanese GP (Suzuka International Racing Course)", "Australian GP (Adelaide Street Circuit)"]
tracks_1992 = ["South African GP (Kyalami Grand Prix Circuit)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Brazilian GP (Autódromo José Carlos Pace)", "Spanish GP (Circuit de Barcelona-Catalunya)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Japanese GP (Suzuka International Racing Course)", "Australian GP (Adelaide Street Circuit)"]
tracks_1993 = ["South African GP (Kyalami Grand Prix Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "European GP (Donington Park)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Japanese GP (Suzuka International Racing Course)", "Australian GP (Adelaide Street Circuit)"]
tracks_1994 = ["Brazilian GP (Autódromo José Carlos Pace)", "Pacific GP (TI Circuit)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "European GP (Circuito Permanente de Jerez)", "Japanese GP (Suzuka Circuit)", "Australian GP (Adelaide Street Circuit)"]
tracks_1995 = ["Brazilian GP (Autódromo José Carlos Pace)", "Argentine GP (Autódromo Oscar Alfredo Gálvez)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "European GP (Nürburgring)", "Pacific GP (TI Circuit)", "Japanese GP (Suzuka Circuit)", "Australian GP (Adelaide Street Circuit)"]
tracks_1996 = ["Australian GP (Albert Park Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "Argentine GP (Autódromo Oscar Alfredo Gálvez)", "European GP (Nürburgring)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Portuguese GP (Autódromo do Estoril)", "Japanese GP (Suzuka Circuit)"]
tracks_1997 = ["Australian GP (Albert Park Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "Argentine GP (Autódromo Oscar Alfredo Gálvez)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Spanish GP (Circuit de Catalunya)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Austrian GP (A1-Ring)", "Luxembourg GP (Nürburgring)", "Japanese GP (Suzuka Circuit)", "European GP (Circuito Permanente de Jerez)"]
tracks_1998 = ["Australian GP (Albert Park Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "Argentine GP (Autódromo Oscar Alfredo Gálvez)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "Austrian GP (A1-Ring)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale Monza)", "Luxembourg GP (Nürburgring)", "Japanese GP (Suzuka Circuit)"]
tracks_1999 = ["Australian GP (Albert Park Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Monaco GP (Circuit de Monaco)", "Spanish GP (Circuit de Catalunya)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "Austrian GP (A1-Ring)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "European GP (Nürburgring)", "Malaysian GP (Sepang International Circuit)", "Japanese GP (Suzuka Circuit)"]
tracks_2000 = ["Australian GP (Albert Park Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "British GP (Silverstone Circuit)", "Spanish GP (Circuit de Catalunya)", "European GP (Nürburgring)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "Austrian GP (A1-Ring)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Indianapolis Motor Speedway)", "Japanese GP (Suzuka Circuit)", "Malaysian GP (Sepang International Circuit)"]
tracks_2001 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Catalunya)", "Austrian GP (A1-Ring)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Nürburgring)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Indianapolis Motor Speedway)", "Japanese GP (Suzuka Circuit)"]
tracks_2002 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Catalunya)", "Austrian GP (A1-Ring)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Nürburgring)", "British GP (Silverstone Circuit)", "French GP (Circuit de Nevers Magny-Cours)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Indianapolis Motor Speedway)", "Japanese GP (Suzuka Circuit)"]
tracks_2003 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Catalunya)", "Austrian GP (A1-Ring)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Nürburgring)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Italian GP (Autodromo Nazionale di Monza)", "United States GP (Indianapolis Motor Speedway)", "Japanese GP (Suzuka Circuit)"]
tracks_2004 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Bahrain GP (Bahrain International Circuit)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "European GP (Nürburgring)", "Canadian GP (Circuit Gilles Villeneuve)", "United States GP (Indianapolis Motor Speedway)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Chinese GP (Shanghai International Circuit)", "Japanese GP (Suzuka Circuit)", "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2005 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Bahrain GP (Bahrain International Circuit)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "European GP (Nürburgring)", "Canadian GP (Circuit Gilles Villeneuve)", "United States GP (Indianapolis Motor Speedway)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Turkish GP (Istanbul Park)", "Italian GP (Autodromo Nazionale di Monza)", "Belgian GP (Circuit de Spa-Francorchamps)", "Brazilian GP (Autódromo José Carlos Pace)", "Japanese GP (Suzuka Circuit)", "Chinese GP (Shanghai International Circuit)"]
tracks_2006 = ["Bahrain GP (Bahrain International Circuit)", "Malaysian GP (Sepang International Circuit)", "Australian GP (Albert Park Circuit)", "San Marino GP (Autodromo Enzo e Dino Ferrari)", "European GP (Nürburgring)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "British GP (Silverstone Circuit)", "Canadian GP (Circuit Gilles Villeneuve)", "United States GP (Indianapolis Motor Speedway)", "French GP (Circuit de Nevers Magny-Cours)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Turkish GP (Istanbul Park)", "Italian GP (Autodromo Nazionale di Monza)", "Chinese GP (Shanghai International Circuit)", "Japanese GP (Suzuka Circuit)",  "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2007 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "United States GP (Indianapolis Motor Speedway)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "European GP (Nürburgring)", "Hungarian GP (Hungaroring)", "Turkish GP (Istanbul Park)", "Italian GP (Autodromo Nazionale di Monza)", "Belgian GP (Circuit de Spa-Francorchamps)", "Japanese GP (Fuji Speedway)", "Chinese GP (Shanghai International Circuit)", "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2008 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Spanish GP (Circuit de Catalunya)", "Turkish GP (Istanbul Park)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit de Nevers Magny-Cours)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "European GP (Valencia Street Circuit)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Fuji Speedway)", "Chinese GP (Shanghai International Circuit)", "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2009 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Chinese GP (Shanghai International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Turkish GP (Istanbul Park)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Hungarian GP (Hungaroring)", "European GP (Valencia Street Circuit)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2010 = ["Bahrain GP (Bahrain International Circuit)", "Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Chinese GP (Shanghai International Circuit)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Turkish GP (Istanbul Park)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Valencia Street Circuit)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka Circuit)", "Korean GP (Korea International Circuit)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2011 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Chinese GP (Shanghai International Circuit)", "Turkish GP (Istanbul Park)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Valencia Street Circuit)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka Circuit)", "Korean GP (Korea International Circuit)", "Indian GP (Buddh International Circuit)", "Abu Dhabi GP (Yas Marina Circuit)", "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2012 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Chinese GP (Shanghai International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Valencia Street Circuit)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka Circuit)", "Korean GP (Korea International Circuit)", "Indian GP (Buddh International Circuit)", "Abu Dhabi GP (Yas Marina Circuit)", "United States GP (Circuit of the Americas)", "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2013 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Chinese GP (Shanghai International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Spanish GP (Circuit de Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "British GP (Silverstone Circuit)", "German GP (Nürburgring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale Monza)", "Singapore GP (Marina Bay Street Circuit)", "Korean GP (Korea International Circuit)", "Japanese GP (Suzuka Circuit)", "Indian GP (Buddh International Circuit)", "Abu Dhabi GP (Yas Marina Circuit)", "United States GP (Circuit of the Americas)", "Brazilian GP (Autódromo José Carlos Pace)"]
tracks_2014 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Chinese GP (Shanghai International Circuit)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka Circuit)", "Russian GP (Sochi Autodrom)", "United States GP (Circuit of the Americas)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2015 = ["Australian GP (Albert Park Circuit)", "Malaysian GP (Sepang International Circuit)", "Chinese GP (Shanghai International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka Circuit)", "Russian GP (Sochi Autodrom)", "United States GP (Circuit of the Americas)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2016 = ["Australian GP (Albert Park Circuit)", "Bahrain GP (Bahrain International Circuit)", "Chinese GP (Shanghai International Circuit)", "Russian GP (Sochi Autodrom)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "European GP (Baku City Circuit)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "Hungarian GP (Hungaroring)", "German GP (Hockenheimring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Malaysian GP (Sepang International Circuit)", "Japanese GP (Suzuka International Racing Course)", "United States GP (Circuit of the Americas)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2017 = ["Australian GP (Albert Park Circuit)", "Chinese GP (Shanghai International Circuit)", "Bahrain GP (Bahrain International Circuit)", "Russian GP (Sochi Autodrom)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Azerbaijan GP (Baku City Circuit)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Malaysian GP (Sepang International Circuit)", "Japanese GP (Suzuka International Racing Course)", "United States GP (Circuit of the Americas)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2018 = ["Australian GP (Albert Park Circuit)", "Bahrain GP (Bahrain International Circuit)", "Chinese GP (Shanghai International Circuit)", "Azerbaijan GP (Baku City Circuit)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit Paul Ricard)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Russian GP (Sochi Autodrom)", "Japanese GP (Suzuka International Racing Course)", "United States GP (Circuit of the Americas)", "Mexican GP (Autódromo Hermanos Rodríguez)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2019 = ["Australian GP (Albert Park Circuit)", "Bahrain GP (Bahrain International Circuit)", "Chinese GP (Shanghai International Circuit)", "Azerbaijan GP (Baku City Circuit)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "French GP (Circuit Paul Ricard)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "German GP (Hockenheimring)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Singapore GP (Marina Bay Street Circuit)", "Russian GP (Sochi Autodrom)", "Japanese GP (Suzuka International Racing Course)", "Mexican GP (Autódromo Hermanos Rodríguez)", "United States GP (Circuit of the Americas)", "Brazilian GP (Autódromo José Carlos Pace)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2020 = ["Austrian GP (Red Bull Ring)", "Styrian GP (Red Bull Ring)", "Hungarian GP (Hungaroring)", "British GP (Silverstone Circuit)", "70th Anniversary GP (Silverstone Circuit)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Belgian GP (Circuit de Spa-Francorchamps)", "Italian GP (Autodromo Nazionale di Monza)", "Tuscan GP (Autodromo internazionale del Mugello)", "Russian GP (Sochi Autodrom)", "Eiffel GP (Nürburgring)", "Portuguese GP (Autódromo Internacional do Algarve)", "Emilia Romagna GP (Autodromo Internazionale Enzo e Dino Ferrari)", "Turkish GP (Istanbul Park)", "Bahrain GP (Bahrain International Circuit)", "Sakhir GP (Bahrain International Circuit)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2021 = ["Bahrain GP (Bahrain International Circuit)", "Emilia Romagna GP (Imola Circuit)", "Portuguese GP (Algarve International Circuit)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Azerbaijan GP (Baku City Circuit)", "French GP (Circuit Paul Ricard)", "Styrian GP (Red Bull Ring)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Monza Circuit)", "Russian GP (Sochi Autodrom)", "Turkish GP (Istanbul Park)", "United States GP (Circuit of the Americas)", "Mexico City GP (Autódromo Hermanos Rodríguez)", "São Paulo GP (Interlagos Circuit)", "Qatar GP (Lusail International Circuit)", "Saudi Arabian GP (Jeddah Corniche Circuit)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2022 = ["Bahrain GP (Bahrain International Circuit)", "Saudi Arabian GP (Jeddah Corniche Circuit)", "Australian GP (Albert Park Circuit)", "Emilia Romagna GP (Imola Circuit)", "Miami GP (Miami International Autodrome)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Monaco GP (Circuit de Monaco)", "Azerbaijan GP (Baku City Circuit)", "Canadian GP (Circuit Gilles Villeneuve)", "British GP (Silverstone Circuit)", "Austrian GP (Red Bull Ring)", "French GP (Circuit Paul Ricard)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Monza Circuit)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka International Racing Course)", "United States GP (Circuit of the Americas)", "Mexico City GP (Autódromo Hermanos Rodríguez)", "São Paulo GP (Interlagos Circuit)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2023 = ["Bahrain GP (Bahrain International Circuit)", "Saudi Arabian GP (Jeddah Corniche Circuit)", "Australian GP (Albert Park Circuit)", "Azerbaijan GP (Baku City Circuit)", "Miami GP (Miami International Autodrome)", "Monaco GP (Circuit de Monaco)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Canadian GP (Circuit Gilles Villeneuve)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Monza Circuit)", "Singapore GP (Marina Bay Street Circuit)", "Japanese GP (Suzuka International Racing Course)", "Qatar GP (Lusail International Circuit)", "United States GP (Circuit of the Americas)", "Mexico City GP (Autódromo Hermanos Rodríguez)", "São Paulo GP (Interlagos Circuit)", "Las Vegas GP (Las Vegas Strip Circuit)", "Abu Dhabi GP (Yas Marina Circuit)"]
tracks_2024 = ["Bahrain GP (Bahrain International Circuit)", "Saudi Arabian GP (Jeddah Corniche Circuit)", "Australian GP (Albert Park Circuit)", "Japanese GP (Suzuka International Racing Course)", "Chinese GP (Shanghai International Circuit)", "Miami GP (Miami International Autodrome)", "Emilia Romagna GP (Imola Circuit)", "Monaco GP (Circuit de Monaco)", "Canadian GP (Circuit Gilles Villeneuve)", "Spanish GP (Circuit de Barcelona-Catalunya)", "Austrian GP (Red Bull Ring)", "British GP (Silverstone Circuit)", "Hungarian GP (Hungaroring)", "Belgian GP (Circuit de Spa-Francorchamps)", "Dutch GP (Circuit Zandvoort)", "Italian GP (Monza Circuit)", "Azerbaijan GP (Baku City Circuit)", "Singapore GP (Marina Bay Street Circuit)", "United States GP (Circuit of the Americas)", "Mexico City GP (Autódromo Hermanos Rodríguez)", "São Paulo GP (Interlagos Circuit)", "Las Vegas GP (Las Vegas Strip Circuit)", "Qatar GP (Lusail International Circuit)", "Abu Dhabi GP (Yas Marina Circuit)"]

current_race_index = 0

# Save and Load Functions
def save_race_result(race_data, filename="race_history.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.extend(race_data)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def save_season_data(season_data, filename="season_history.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(season_data)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def view_race_history(filename="race_history.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            
            history_label = ttk.Label(history_tab, text="Race History", font=("Arial", 16, "bold"))
            history_label.pack(pady=10)
            for race in data:
                track = race["track"]
            Race_name = ttk.Label(history_tab, text= track, font=("Arial", 14, "bold"))
            Race_name.pack(pady=10)

            for race in data:
                race_position = race["race_position"]
                driver = race["driver"]
                team = race["team"]
                performance = race["performance"]
                dnf = "DNF" if race["dnf"] else f"{performance:.2f} pts"
                points = f" [+{race['points']}]" if race['points'] > 0 else ""

                race_result_text = f"- Position {race_position}: {driver} ({team}) - {dnf}{points}"
                ttk.Label(history_tab, text=race_result_text, font=("Arial", 12)).pack()

    except FileNotFoundError:
        print("No race history found.")


def view_past_seasons(filename="season_history.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for season in data:
                print(f"\U0001F3C6 {season['season']} Champion: {season['drivers_champion']} ({season['constructors_champion']})")
                print("Race Winners:")
                for race in season["race_winners"]:
                    for gp, winner in race.items():
                        print(f"- {gp}: {winner}")
                print("\n")
    except FileNotFoundError:
        print("No history available.")

# Classes
class Team:
    def __init__(self, name, budget, car_performance):
        self.name = name
        self.budget = budget
        self.car_performance = car_performance
        self.reliability = 70
        self.drivers = []

    def assign_driver(self, driver):
        self.drivers.append(driver)
        driver.team = self

class Driver:
    def __init__(self, name, age, skill, aggression, consistency):
        self.name = name
        self.age = age
        self.skill = skill  
        self.aggression = aggression  
        self.consistency = consistency  
        self.team = None
        self.points = 0

teams = []

def setup_season(year=1950):
    global teams 

    if not teams: 
        active_teams = []
        for team_data in teams_1950:
            team = Team(team_data["name"], team_data["budget"], team_data["performance"])
            active_teams.append(team)
        
        for team in active_teams:
            for _ in range(2):
                driver = generate_new_driver()
                team.assign_driver(driver)
        
        teams = active_teams  
    return teams

def calculate_age(dob):
    if isinstance(dob, np.datetime64):
        dob = pd.to_datetime(dob)

    if isinstance(dob, pd.Timestamp):
        dob = dob.to_pydatetime()

    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  
    return age

def generate_new_driver():
    file_path = "F1 driver list.xlsx"
    df = pd.read_excel(file_path)

    df["Date of Birth"] = pd.to_datetime(df["Date of Birth"], format="%d/%m/%Y", errors="coerce")

    today = datetime.today()

    df["Age"] = today.year - df["Date of Birth"].dt.year
    df["Age"] -= (today < df["Date of Birth"].apply(lambda dob: dob.replace(year=today.year)))

    eligible_names = df[(df["Age"] > 17)]["Driver name"].dropna().tolist()

    if not eligible_names:
        print("No eligible drivers found.")
        return None

    random_name = random.choice(eligible_names)
    age = calculate_age(df[df["Driver name"] == random_name]["Date of Birth"].values[0])  
    skill = random.randint(50, 99)
    aggression = random.randint(40, 90)
    consistency = random.randint(50, 100)

    return Driver(random_name, age, skill, aggression, consistency)


def retire_and_replace_drivers(drivers):
    new_drivers = []
    for driver in drivers:
        if driver["age"] > 35 and random.random() > 0.5:
            print(f"{driver['name']} has retired!")
        else:
            new_drivers.append(driver)

    for _ in range(random.randint(1, 2)):
        new_drivers.append(generate_new_driver())
    
    return new_drivers


def simulate_race(teams):
    global current_race_index

    current_track = tracks_1950[current_race_index]
    all_drivers = []
    for team in teams:
        all_drivers.extend(team.drivers)
        
    
    results = []
    for driver in all_drivers:
        base_performance = (driver.skill * 0.6) + (driver.team.car_performance * 0.4)
        
        random_factor = (random.randint(-30, 30)) 
        
        consistency_factor = driver.consistency / 100
        adjusted_randomness = random_factor * (1 - consistency_factor)
        
        race_performance = base_performance + adjusted_randomness
        
        reliability_check = random.random() * 100
        dnf = reliability_check > driver.team.reliability
        
        results.append({
            "driver": driver,
            "team": driver.team,
            "performance": race_performance,
            "dnf": dnf
        })
    
    results.sort(key=lambda x: (-999 if x["dnf"] else x["performance"]), reverse=True)
    
    points_system = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    
    result_strings = []
    race_results =[]
    for index, result in enumerate(results):
        position = index + 1
        points = 0
        
        if not result["dnf"] and position <= 10:
            points = points_system[index]
            result["driver"].points += points
        
        if position == 1:
            points += 1
            result["driver"].points += 1
        
        status = "DNF" if result["dnf"] else f"{result['performance']:.2f} pts"
        points_display = f" [+{points}]" if points > 0 else ""

        result_strings.append(f"{position}. {result['driver'].name} ({result['team'].name}) - {status}{points_display}")
    
        race_results.append({
            "track": current_track,
            "race_position": position,
            "driver": result["driver"].name,
            "team": result["team"].name,
            "performance": result["performance"],
            "dnf": result["dnf"],
            "points": points
        })

    save_race_result(race_results)
    return result_strings


def race_simulation_window():
    global current_race_index
    race_window = tk.Toplevel(root)
    race_window.title("Race Simulation")
    race_window.geometry("600x600")
    ttk.Label(race_window, text="Race Simulation Running...", font=("Arial", 14)).pack(pady=10)
    
    teams = setup_season()
    results = simulate_race(teams)
    ttk.Label(race_window, text=("\U0001F3C1 Final Race Results for \U0001F3C1" + tracks_1950[current_race_index]), font=("Arial", 16, "bold")).pack(pady=10)
    current_race_index = (current_race_index + 1) % len(tracks_1950)

    for result in results:
        ttk.Label(race_window, text=result, font=("Arial", 12)).pack()


def open_race_simulation():
    race_simulation_window()

# GUI
root = tk.Tk()
root.title("F1 Manager - Historic Mode")
root.geometry("800x600")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)
home_tab = ttk.Frame(notebook)
general_tab = ttk.Frame(notebook)
history_tab = ttk.Frame(notebook)
notebook.add(home_tab, text="Home")
notebook.add(general_tab, text="General")
notebook.add(history_tab, text="History")
view_history_btn = ttk.Button(history_tab, text="View Race History", command=view_race_history)
view_history_btn.pack(pady=10)
start_race_btn = ttk.Button(general_tab, text="Start Race Simulation", command=open_race_simulation)
start_race_btn.pack(pady=10)
root.mainloop()


'''
TO-DO List
-Make windows scrollable
-History tab currently does the same race over and over
-Make drivers consistant for year you are in
-Dont just refference a certain year, need to be broad for when other seasons come into it
-Automatic history?
-Be able to go through seasons, new teams - same drivers or completely new?
-Once a driver has been chosen remove from available drivers
-Get a way of tracking points per season for drivers and constructors.
-Save season data
-Be able to use other functions, - retiring drivers
-Make it look pretty
-Race result display - grid
'''