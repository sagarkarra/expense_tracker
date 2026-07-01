import tkinter as tk
from tkinter import ttk, messagebox

class DynamicExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("620x540")
        
        # 1. DATA STORAGE (Concept: Lists)
        # Storing rows as element sequences inside a primary container array list
        self.expenses = []
        
        # --- GRAPHIC INTERFACE LAYOUT FRAMES ---
        budget_frame = ttk.LabelFrame(root, text=" ⚙️ Target Budget Control Panel ", padding=10)
        budget_frame.pack(fill="x", padx=15, pady=8)
        
        input_frame = ttk.LabelFrame(root, text=" ➕ Add New Transaction Entry ", padding=10)
        input_frame.pack(fill="x", padx=15, pady=8)
        
        table_frame = ttk.Frame(root, padding=10)
        table_frame.pack(fill="both", expand=True, padx=15)
        
        button_frame = ttk.Frame(root, padding=5)
        button_frame.pack(fill="x", padx=15)

        # --- BUDGET FRAME COMPONENTS (Extra Advanced Feature) ---
        ttk.Label(budget_frame, text="Set Custom Budget Ceiling Limit: ₹").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.budget_entry = ttk.Entry(budget_frame, width=15, font=("Arial", 10, "bold"))
        self.budget_entry.grid(row=0, column=1, padx=5, pady=5)
        self.budget_entry.insert(0, "5000.00") # Starts with 5000 as a smart initial default value
        
        btn_update_budget = ttk.Button(budget_frame, text="🔒 Lock & Apply Budget", command=self.calculate_total)
        btn_update_budget.grid(row=0, column=2, padx=15, pady=5)

        # --- TRANSACTION INPUT COMPONENTS ---
        ttk.Label(input_frame, text="Item Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.desc_entry = ttk.Entry(input_frame, width=18)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Amount (₹):").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(input_frame, width=12)
        self.amount_entry.grid(row=0, column=3, padx=5, pady=5)
        
        btn_add = ttk.Button(input_frame, text="Add Expense", command=self.add_expense)
        btn_add.grid(row=0, column=4, padx=15, pady=5)
        
        # --- TREEVIEW DATA GRID SPREADSHEET TABLE ---
        columns = ("desc", "amount")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=9)
        self.tree.heading("desc", text="Expense Item Description")
        self.tree.heading("amount", text="Amount Spent (₹)")
        
        # Visual Table Matrix Center Alignment Rules
        self.tree.column("desc", width=260, anchor="center")  
        self.tree.column("amount", width=160, anchor="center") 
        self.tree.pack(fill="both", expand=True)

        # --- GRID MANAGEMENT CONTROL BUTTONS ---
        btn_delete = ttk.Button(button_frame, text="🗑️ Delete Highlighted Row", command=self.delete_selected)
        btn_delete.pack(side="left", padx=5)
        
        btn_clear = ttk.Button(button_frame, text="🔄 Master Reset Ledger Data", command=self.clear_all)
        btn_clear.pack(side="left", padx=5)
        
        # --- CALCULATION RESULTS PANEL ---
        self.total_label = ttk.Label(root, text="Total Spending: ₹0.00", font=("Arial", 14, "bold"), foreground="darkgreen")
        self.total_label.pack(pady=15)

    # =========================================================================
    # CORE REQUIRMENT ENGINE METHODS
    # =========================================================================
    
    # FEATURE 1: Add Expenses to Storage Objects List Arrays
    def add_expense(self):
        desc = self.desc_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        
        if not desc:
            messagebox.showerror("Validation Error", "Item description text cannot be left blank!")
            return
            
        try:
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showerror("Validation Error", "Transaction calculation entry values must exceed zero!")
                return
        except ValueError:
            messagebox.showerror("Data Type Error", "Please parse numerical values inside the amount row entry frame!")
            return
            
        # Append data pair entry to the local array matrix tracker list structure
        self.expenses.append((desc, amount))
        
        # Insert target data values dynamically inside the centered table layout cells
        self.tree.insert("", tk.END, values=(desc, f"₹{amount:.2f}"))
        
        # Clear specific view data input field states
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        
        # Run recalculation pipeline logic updates loop triggers
        self.calculate_total()

    # EXTRA FEATURE: Erase Target Item Out of Tracking List Elements Arrays
    def delete_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Warning", "Please left-click a data row inside the spreadsheet layout first!")
            return
            
        # Track relative layout coordinate mapping matrix indices pointers
        index = self.tree.index(selected_item)
        
        # Evict item accurately from tracking context array data tracking list structures
        self.expenses.pop(index)
        
        # Delete on-screen UI row block element
        self.tree.delete(selected_item)
        
        # Refresh the master budget balances calculations
        self.calculate_total()
        messagebox.showinfo("Operation Complete", "Selected data log record cleared from active array instances.")

    # EXTRA FEATURE: Full Scope Core Variable Clear Functions Reset Commands
    def clear_all(self):
        if not self.expenses:
            return
            
        if messagebox.askyesno("Confirm Reset Action", "Are you sure you want to flush all records out of your list tracking history?"):
            self.expenses.clear() # Erase background dynamic container array list completely
            
            for item in self.tree.get_children():
                self.tree.delete(item) # Flush GUI row frame elements
                
            self.calculate_total()

    # CONCEPT REQUIRMENT: Dynamic Mathematical Computations System Triggers
    def calculate_total(self):
        # Accumulate loop summation over specific item values arrays trackers list indices elements
        total_spending = sum(item[1] for item in self.expenses)
        self.total_label.config(text=f"Total Spending: ₹{total_spending:.2f}")
        
        # Safely capture current user runtime input boundary settings configuration targets
        try:
            user_budget_ceiling = float(self.budget_entry.get().strip())
            if user_budget_ceiling < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Config Error", "Invalid budget value entry! Restoring basic ₹5,000.00 baseline safety threshold parameters.")
            user_budget_ceiling = 5000.00
            self.budget_entry.delete(0, tk.END)
            self.budget_entry.insert(0, "5000.00")
            
        # DYNAMIC BUDGET CHECKS: Algorithmic conditional switch verification loops
        if total_spending > user_budget_ceiling:
            self.total_label.config(foreground="red") # Visual alert theme trigger activation state
            messagebox.showwarning("Budget Threshold Warning", f"🚨 Alert! Total expenditure balances have overshot your allocated ₹{user_budget_ceiling:.2f} ceiling limit threshold tracker matrix parameters!")
        else:
            self.total_label.config(foreground="darkgreen") # Safe configuration restore behavior standard state

# System Boot Sequence Entry Pipeline
if __name__ == "__main__":
    root = tk.Tk()
    app = DynamicExpenseTracker(root)
    root.mainloop()
