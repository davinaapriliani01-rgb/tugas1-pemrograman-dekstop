import sqlite3
from database import get_connection

class User:
    """Model untuk User"""
    
    @staticmethod
    def login(username, password):
        """Login pengguna"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users 
            WHERE username = ? AND password = ?
        ''', (username, password))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None
    
    @staticmethod
    def get_all_mahasiswa():
        """Get all mahasiswa"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE role = "mahasiswa" ORDER BY nama')
        users = cursor.fetchall()
        conn.close()
        return [dict(user) for user in users]
    
    @staticmethod
    def get_all_users():
        """Get all users"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY nama')
        users = cursor.fetchall()
        conn.close()
        return [dict(user) for user in users]

    @staticmethod
    def create(username, password, role, nama):
        """Tambah user baru"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, password, role, nama)
                VALUES (?, ?, ?, ?)
            ''', (username, password, role, nama))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def delete(user_id):
        """Hapus user berdasarkan ID (beserta data absensinya)"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM absensi WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted